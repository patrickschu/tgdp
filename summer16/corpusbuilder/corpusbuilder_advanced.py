#!/usr/bin/env python

import json
import os
import codecs
import re
import argparse
import sys
import operator
import shutil
import time


##NOTE THAT THIS IS DIFFERENT in PY3

import Tkinter 
import tkFileDialog


###global variables###

regexdict={
'speaker_regex':"\d+-(\d+)-\d+.zip"
}
speaker_regex="\d+-(\d+)-\d+.*[wav|zip]"
header="\n-----\n"


#the operatordict matches functions to inputstrings
operatordict={
"<":operator.lt,
"<=": operator.le,
"==":operator.eq,
"=":operator.eq,
"!=":operator.ne,
">=":operator.ge,
">":operator.gt
}


###helper functions###
def check_input(*args):
	"""
	Checks if directories supplied as args actually exist
	"""
	for arg in args:
		if not os.path.isdir(arg):
			raise IOError("The directory '{}' can't be found. Make sure it exists at this location.".format(arg))



def jsonreader(json_file, repair_formatting):
	"""
	Takes a JSON file with informant data, returns a dictionary with 1 entry per speaker ID. 
	Output format: {1: {current_residence: XYZ, speaker_id: XZY, ..},{2:{}}
	Repairs faulty JSON formatting if repair_formatting = True; reduces DOB entries to 4 characters. 
	Lowercases all string data. 
	"""
	inputdata=codecs.open(json_file, "r", "utf-8").read()
	inputdata=re.findall("\[\{.*\}\]", inputdata)
	if len(inputdata) < 1:
		raise IOError("Cannot extract the JSON data. Make sure the relevant section starts with '[{' and ends with '}]'.")
	inputdata=inputdata[0]
	print "Reading JSON data from file '{}'. The file is {} characters long".format(json_file, len(inputdata))
	# thank you SO: http://stackoverflow.com/questions/37689400/dealing-with-mis-escaped-characters-in-json
	if repair_formatting:
		print "Repair formatting on."
		inputdata = re.sub(r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'', inputdata)
	try: 
		jsondata=json.loads(inputdata)
	except ValueError, err:
		raise ValueError("{} {}".format (err, "\nCannot read the JSON data, try setting 'repair_formatting' to 'True'."))
	informantdicti={}
	count=0
	for datapoint in jsondata:
		count=count+1
		informantdicti[count]={k:v.lower() if isinstance(v,basestring) else v for k,v in datapoint.items() }
	for entry in informantdicti:
		informantdicti[entry]['DOB']=int(informantdicti[entry]['DOB'].split("-")[0])
	return informantdicti


def valuegetter(dict, key, operator_string, value):
	"""
	Uses the operation defined in operator_string to match the input value to entries in dict.
	It reads the operators from the operatordict. 
	Prints warning if not value (i.e. dictionary value: None or no parameter (i.e. dictionary lacks key). 
	Returns matches in resultlist, errors in no_value and no_key. 
	"""
	if not operatordict.get(operator_string, None):
		raise TypeError("The operator '{}', supplied with the parameter '{}', is not valid\n". format(operator_string, key))
	else:
		operator=operatordict[operator_string]
		results={i:dict[i] for i in dict if operator(dict[i].get(key, None),value)}
		
		no_value={i for i in dict if dict[i].get(key)==None}
		if no_value:
			print "There are no values for this parameter in these files: ", [str(i) for i in no_value]
		no_key={i for i in dict if key not in dict[i].keys()}
		if no_key:
			print "There is no such category in these files: ", [str(i) for i in no_key]
		return results, no_value, no_key



###MAIN####

def main():

	##inputting JSON
	print header, "Running the corpusbuilder."
	print "Please choose JSON file containing informant metadata."
	root=Tkinter.Tk()
	root.withdraw()
	root.update()
	#json_file=tkFileDialog.askopenfilename(title="Please choose JSON file containing informant metadata")
	json_file=os.path.expanduser(os.path.join("~/Desktop", "database", "informants.json"))
	informantdicti=jsonreader(json_file, repair_formatting=True)
	#collect keys, i.e. possible input 
	keys=[v.keys() for k,v in informantdicti.items()]
	keys=[item for listi in keys for item in listi]
	
	#informantdicti[0]={'gender':None, 'DOB':1999}
	keys=list(set(keys))
	print keys	

	#set up input arguments
	parser = argparse.ArgumentParser()
	for key in keys:
		parser.add_argument("--"+key, type=str, help="Possible input to the argument '{}' includes: {:.1500} ".format(key, ", ".join(set([str(informantdicti[e].get(key)) for e in informantdicti]))))
	args = parser.parse_args()
	argsdict=vars(args)
	if set(argsdict.values()) == set([None]):
		print "Warning: You did not enter any conditions to select data. Use the '--help' command to see your options."
	print set([str(informantdicti[e].get("current_residence", None)) for e in informantdicti])
# 	for residence in set([str(informantdicti[e].get("current_residence")) for e in informantdicti]):
# 		if len(residence) > 0:
# 		#print set([str(informantdicti[e].get("current_residence", None)) for e in informantdicti])
# 			print residence
# 			filename=os.path.expanduser(os.path.join("~/Desktop/txgdp_out", residence, "gilbert"))
# 			print filename
# 			os.makedirs(filename)
	
	
	#setting up in and out
	
	print "Please choose a directory that contains your corpus files"
	root=Tkinter.Tk()
	root.withdraw()
	##inputdir manually. only for lazy people
	#inputdir="TXGDP/interviews" ['/Volumes/TXGDP/interviews']

	inputdir=[os.path.expanduser(os.path.join("~/Desktop/gilbert_unzipped", str(i))) for i in range(1,149)]
	#inputdir = [tkFileDialog.askdirectory(title="Inputfolder: Please choose a directory that contains your corpus files")]
	#print inputdir
	print "Please choose a directory to copy files into."
	root=Tkinter.Tk()
	root.withdraw()
	root.update()
	#outputdir = tkFileDialog.askdirectory(title="Outputfolder: Please choose a directory to copy files into")
	outputdir=os.path.expanduser(os.path.join("~/Desktop", "txgdp_out"))
	#print "{}'{}' set as input folder".format(header, ", ".join(inputdir))
	print "'{}' set as output folder {}".format(outputdir, header)
	#check_input(outputdir,*inputdir)
	inputfilis=[]
	for dir in inputdir:
		inputfilis.append([i for i in os.listdir(dir) if re.match(speaker_regex, i)])
	inputfilis=[item for listi in inputfilis for item in listi]
	print len(inputfilis)
	#iterate over all arguments, collect in resultlist
	resultlist=[]
	for entry in set([str(informantdicti[e].get("current_residence")) for e in informantdicti]):
		print type(entry)
		print entry
		intinput=re.compile("(["+"".join(operatordict.keys())+"]+)(?:\s*?)([0-9]+)")
		strinput=re.compile("(["+"".join(operatordict.keys())+"]+)(?:\s*?)(.+)")
		if re.match(strinput, "="+entry):
			print "match"
			if len(entry) > 0:
				print "length"
				#what if they try to use > or < with a string
				matcher=re.findall(strinput, "="+entry)[0]
				print matcher
				#print "Matching ", entry, " ".join(matcher)
				print str(matcher[1])
				#dict, key, operator_string, value
				results, no_value, no_key = valuegetter(informantdicti, "current_residence", matcher[0], str(matcher[1]))
				#print results	
				resultlist.append(results)
		else:
			print "\nError: No match for the input ", entry
		speaker_ids= [str(informantdicti[i].get("informant_id")) for i in results]
		print speaker_ids
		for speaker_id in speaker_ids:
			speaker_entry={k:v for k,v in informantdicti.items() if v.get("informant_id") == int(speaker_id)}
			json.dump(speaker_entry, file(os.path.join(outputdir, entry, "speaker"+speaker_id+".txt"), 'w'))
			#switch back on for basic input
			#files_to_copy=[i for i in inputfilis if re.findall(speaker_regex, i)[0] == speaker_id]
			for dir in inputdir:
				#print os.listdir(dir)
				all_files=[i for i in os.listdir(dir) if re.match(speaker_regex, i)]
				files_to_copy=[i for i in all_files if re.findall(speaker_regex, i)[0] == speaker_id]
				print speaker_id, files_to_copy		
				if len(files_to_copy) > 0:
					for fili in files_to_copy:
						shutil.copy2(os.path.join(dir, fili), os.path.join(outputdir,entry,"gilbert",fili))
						print "Copied '{}' to '{}'".format(os.path.join(dir, fili), os.path.join(outputdir,entry, "gilbert",fili))
		
			#speaker_entry={k:v for k,v in informantdicti.items() if v.get("informant_id") == int(speaker_id)}
		
		#json.dump(speaker_entry, file(os.path.join(outputdir,"speaker"+speaker_id+".txt"), 'w'))
	print "resultlist", resultlist[0]
	# resultlist_keys=[i.keys() for i in resultlist]
# 	print "resultlist", resultlist[0]
# 	sharedresultlist=[i.keys() for i in resultlist]
	#sharedresultlist=set.intersection(*[set(i) for i in resultlist_keys])
	print "{}{} speakers meet the criteria:".format(header, len(sharedresultlist))
	
	
	sharedresultspeakers=[str(informantdicti[i]["informant_id"]) for i in sharedresultlist]
	print "IDs {}".format(", ".join(sharedresultspeakers))
	for speaker_id in sharedresultspeakers:
		speaker_entry={k:v for k,v in informantdicti.items() if v.get("informant_id") == int(speaker_id)}
		
		json.dump(speaker_entry, file(os.path.join(outputdir,"speaker"+speaker_id+".txt"), 'w'))
		#switch back on for basic input
		#files_to_copy=[i for i in inputfilis if re.findall(speaker_regex, i)[0] == speaker_id]
		for dir in inputdir:
			#print os.listdir(dir)
			all_files=[i for i in os.listdir(dir) if re.match(speaker_regex, i)]
			files_to_copy=[i for i in all_files if re.findall(speaker_regex, i)[0] == speaker_id]
			print speaker_id, files_to_copy		
			if len(files_to_copy) > 0:
				for fili in files_to_copy:
					shutil.copy2(os.path.join(dir, fili), os.path.join(outputdir,fili))
					print "Copied '{}' to '{}'".format(os.path.join(dir, fili), os.path.join(outputdir,fili))
			# else:
# 				print "There are no files associated with speaker ID {} in location '{}'`".format(speaker_id, inputdir)
		
	print header, "Corpus builder exited."



if __name__ == "__main__":
    main()













