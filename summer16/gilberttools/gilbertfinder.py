# -*- coding: utf-8 -*-

##getting relevant gilbert files

import pandas
import argparse
import numpy as np
import operator
import re
import os
import shutil
import Tkinter 
import tkFileDialog
import sys
import codecs
import json
 
#tools
header="\n\n---\n"

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

voweldict={}




#helper functions

def jsonreader(json_file, fix_formatting_off):
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
	if not fix_formatting_off:
		print "Fix formatting on."
		inputdata = re.sub(r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'', inputdata)
	try: 
		jsondata=json.loads(inputdata)
	except ValueError, err:
		raise ValueError("{} {}".format (err, "\nCannot read the JSON data, try changing the setting for 'fix_formatting'."))
	informantdicti={}
	count=0
	for datapoint in jsondata:
		count=count+1
		informantdicti[count]={k:v.lower() if isinstance(v,basestring) else v for k,v in datapoint.items() }
	for entry in informantdicti:
		informantdicti[entry]['DOB']=int(informantdicti[entry]['DOB'].split("-")[0])
	return informantdicti
	
	
def gilbertfileanalyzer(filename, informant_dicti):
	"""
	The gilbertfileanalyzer takes the name of a Gilbert sound file and a dictionary w/ informant metadata.
	It parses the filename to return speaker metadata.
	Metadata comes as a list of [speaker_number, gilbert_number, interviewer_number, location, gender, date_of_birth]
	"""
	print filename
	regex='(\d+)-(\d+)-(\d+)-(\d+)-(\D+)\.wav'
	res=re.findall(regex,filename)[0]
	if len(res) != 5:
		raise ValueError("'{}' does not match the pattern for Gilbert files.".format(filename))
	iver_number, speaker_number, unknown_thing, gilbert_number, random_character = res
		#informant_id is where speaker number lives
	meta=[informant_dicti[f] for f in informant_dicti if informant_dicti[f].get('informant_id', None) == int(speaker_number)]
	
	if len(meta) != 1:
		raise ValueError("No unambiguous match for speaker ID '{}' extracted out of file '{}'.".format(speaker_number, filename))
	
	meta=meta[0]
	#here we extract metadata to include in the spreadsheet
	location, gender, dob = [meta.get('current_residence', None), meta.get('gender', None), meta.get('DOB', None)]
	return speaker_number, gilbert_number, iver_number, location, gender, dob



def extracter(spreadsheet, column_name, sound):
	"""
	The extracter moves files.
	Arguments input_folder and output_folder are set through GUI. 
	Based on the values in the column called column_name in the spreadsheet, files are copied from input_folder to output_folder. 
	Here, these are the gilbert_numbers in the spreadsheet fed from main(). 
	The are matched to the file names. 
	Each gilber_number gets its own directory in the output_folder. 
	output_folder should be empty, at least not contain the same gilbert_numbers already.
	Also copies all speaker files from input_folder to output_folder. 
	"""
	print header, "Running the extracter."
	#this can also be set interactively if we feel like it
	informantdicti=jsonreader('/Users/ps22344/Desktop/database/informants.json',False)
	#better if we had this as json as well
	gilbertdata=pandas.read_csv('/Users/ps22344/Downloads/tgdp-master/summer16/files/gilbert_questions_withtrans_final.csv', encoding="utf-8")
	#make a func that automates this Tkinter bizness
	print "Please choose a directory that contains your sound files."
	# root=Tkinter.Tk()
# 	root.withdraw()
# 	root.update()
# 	input_folder=tkFileDialog.askdirectory(title="Inputfolder: Please choose a directory that contains your corpus files")
	input_folder='/Users/ps22344/Desktop/txgdp_by_location_more_than_3_spkrs'
	print "Please choose a directory that you want your files to be copied into."
	root=Tkinter.Tk()
	root.withdraw()
	root.update()
	output_folder=tkFileDialog.askdirectory(title="Outputfolder: Please choose a directory to copy files into")
	print header, "Copying files from '{}' to '{}'.".format(input_folder, output_folder)
	#collecting input files
	inputfiles=[]
	print "Locating files."
	for dirpath, subdirs, files in os.walk(input_folder):
		for f in files:
			inputfiles.append(os.path.join(dirpath, f))
			if len(inputfiles) in [1000,2000,4000,8000,16000,24000]:
				print "{} files processed, still working.".format(len(inputfiles))
	print "Found {} files.".format(len(inputfiles))
	numbers_to_be_extracted= spreadsheet[column_name].unique()
	print header, "Gilbert numbers to be extracted:"
	print ",".join([unicode(i) for i in numbers_to_be_extracted])
	#copying speaker files
	print header, "Copying speaker files."
	speakerfiles=[f for f in inputfiles if re.match(".*\.txt", os.path.split(f)[1])]
	os.mkdir(os.path.join(output_folder, "speakers"))
	for s in speakerfiles:
		shutil.copy2(s, os.path.join(output_folder, "speakers"))
	#finding relevant input files
	result=[]
	for number in numbers_to_be_extracted:
		print "Processing {}, creating folder '{}'.".format(number, number)
		os.mkdir(os.path.join(output_folder, unicode(number)))
		#MAKE A SPREADSHEET NAMED AFTER GILBERT FILE
		gilbert_sentence=gilbertdata[gilbertdata['gilbert_number']==number]
	 	column_dict={
		'id':[],
		'file_name':[],
		'speaker_number':[], 
		'gilbert_number':[], 
		'iver_number':[], 
		'location':[], 
		'gender':[], 
		'dob':[],
		'variable':[],
 		'input_form':[],
 		'target_form':[],
 		'transcription':[],
 		'pre_sound':[],
 		'post_sound':[]
		}
	
		
		regex="(\d+)-(\d+)-(\d+)-"+number.astype('U')+"-(\D+)\.wav"
		findings= [f for f in inputfiles if re.match(regex, os.path.split(f)[1])]
		result= result+findings
		for find in findings:
			os.path.split(find)[1]
			shutil.copy2(find, os.path.join(output_folder, unicode(number), os.path.split(find)[1]))
			speaker_number, gilbert_number, iver_number, location, gender, dob=gilbertfileanalyzer(os.path.split(find)[1], informantdicti)
			
			column_dict['id'].append(os.path.split(find)[1])
			column_dict['file_name'].append(find)
			column_dict['speaker_number'].append(speaker_number)
			column_dict['gilbert_number'].append(gilbert_number)
			column_dict['iver_number'].append(iver_number)
			column_dict['location'].append(location)
			column_dict['gender'].append(gender)
			column_dict['dob'].append(dob)
			column_dict['variable'].append(sound)
 			column_dict['input_form'].append(gilbert_sentence['input_form'].iloc[0])
 			column_dict['target_form'].append(gilbert_sentence['target_form'].iloc[0])
 			column_dict['transcription'].append(gilbert_sentence['transcription'].iloc[0])
 			
 			splitstring=list(gilbert_sentence['transcription'].iloc[0])
 			#print splitstring
 			indexi=splitstring.index(sound.decode('utf-8'))
 			#print indexi
 			# pre=splitstring[indexi-1]
#  			
#  			#post=splitstring[indexi+1]
 			
 			#print pre, post
 			
 			
 			
 			column_dict['pre_sound'].append(splitstring[indexi-1])
 			column_dict['post_sound'].append(splitstring[indexi+1])
		
		
		
# 		test="aɪnə"
# 		#test="eine"
# 		print test
# 		variable="ɪ"
# 		print variable
# 		rr= list(test.decode('utf-8'))
# 		print rr
# 		s=rr.index(variable.decode('utf-8'))
# 		print s
# 		pre=rr[s-1]
# 		post=rr[s+1]
# 		print pre, post
# 		
#		print column_dict
		for e in column_dict:
			print e, 'length', len(column_dict[e])
		metadata_spreadsheet=pandas.DataFrame(column_dict)
		#print metadata_spreadsheet
		metadata_spreadsheet.to_csv(os.path.join(output_folder, unicode(number), str(number)+".csv"), encoding="utf-8")
	print header, "{} files have been copied to {}.".format(len(result), output_folder)


###MAIN###

##Note that some gilbert_numbers apply to several sentences. (all up to #20).
def main():
	"""
	Matches gilbert_sentences as contained in the inputfile to user input. 
	Input can be numeric (e.g. entries in inputfile[items] that are = 2).
	Input can be characters (e.g. all entries in inputfile[transcription] that contain 'ɪ').
	If output_csv is set, the resulting data will be written to a csv file. 
	If move_data is set, the resulting data will be used to copy the relevant files to desired folder. 
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument("input_file", type=str, help="The input_file is the spreadsheet containing the Gilbert sentence numbers, target forms, etc.")
	initial_args, extras=parser.parse_known_args()
	print initial_args.input_file
	print header, "Running the sentence finder", header
	with open(initial_args.input_file, "r") as inputspread:
		inputdata=pandas.read_csv(inputspread, encoding="utf-8")
	
	#temporary until new csv file
	#inputdata=inputdata['gilbert_number'].astype(float)
	#building up criteria	
	for c in inputdata.columns:
		parser.add_argument("--"+c, type=lambda s: unicode(s, 'utf8'))
	parser.add_argument("--move_data", action='store_true', help="If this flag is set, files that match criteria are copied from input_folder to output_folder. input_folder and output_folder are set through graphical interface.")
	parser.add_argument("--output_csv", action='store_true', help="If set, this flag is set, a csv file containing the sentences that match the criteria is written. The output_folder is set through graphical interface.")
	args= parser.parse_args()
	argsdict= vars(args)
	intinput=re.compile(ur"(["+"".join(operatordict.keys())+"]+)(?:\s*?)([0-9]+)", re.UNICODE)
	strinput=re.compile(ur"(["+"".join(operatordict.keys())+"]+)(?:\s*?)(\D+)", re.UNICODE)
	#this needs to happen because we construct the final dataset by taking things out of the inputdata
	outputdata= inputdata
	
	#the actual matching happens here, two procedures for strings versus numbers
	#in every iteration, we keep only the intersection btw the two dataframes
	for item in [a for a in argsdict if argsdict[a] and a in inputdata.columns]:
		print "Processing", type(argsdict[item])
		if re.match(strinput, argsdict[item]):
			#what if they try to use > or < with a string
			matcher=re.findall(strinput, argsdict[item])[0]
			print "Matching string", item, " ".join(matcher)
			outputdata=pandas.merge(outputdata, inputdata[inputdata[item].str.contains(matcher[1])], how='inner')
		elif re.match(intinput, argsdict[item]):
			matcher=re.findall(intinput, argsdict[item])[0]
			print "Matching number", item, " ".join(matcher)
			outputdata=pandas.merge(outputdata, inputdata[operatordict[matcher[0]](inputdata[item], float(matcher[1]))], how='inner')
		else:
			print "\nError: No match for the input", item
	print header, "Resulting dataset:"
	print outputdata	
	if argsdict['output_csv']:
		print header, "output_csv is activated."
		print "Please choose a directory and file name to save the csv file to."
		root=Tkinter.Tk()
		root.withdraw()
		root.update()
		output_csv = tkFileDialog.asksaveasfile(mode='w', defaultextension=".csv", title="Choose file name for csv output.")
		#output_csv=tkFileDialog.askopenfilename(title="Please choose file name for csv output.")
		outputdata.to_csv(output_csv, encoding="utf-8", index=False)
		print header, "Written csv spreadsheet to {}".format(output_csv)
	if argsdict['move_data']:
		print header, "move_data is activated."
		extracter(outputdata, 'gilbert_number', 'ɪ')
	
	
 
#main('/Users/ps22344/Downloads/tgdp-master/summer16/files/gilbert_questions_withtrans_final.csv', 'transcription', 'deːɐ̯', '/Users/ps22344/Downloads/tgdp-master/summer16/files/testsentencefinder.csv')


if __name__ == "__main__":
	main()