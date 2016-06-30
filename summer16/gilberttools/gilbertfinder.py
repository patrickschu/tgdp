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



#helper functions
def extracter(spreadsheet, column_name):
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
 	print "Please choose a directory that contains your sound files."
 	root=Tkinter.Tk()
	root.withdraw()
	root.update()
 	input_folder=tkFileDialog.askdirectory(title="Inputfolder: Please choose a directory that contains your corpus files")
 	"Please choose a directory that you want your files to be copied into."
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
 	#read from spreadsheet
 	# with open(spreadsheet, "r") as spreadsheet:
#  		spreadsheet=pandas.read_csv(spreadsheet, encoding="utf-8")
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
		regex="(\d+)-(\d+)-(\d+)-"+number.astype('U')+"-(\D+)\.wav"
  		findings= [f for f in inputfiles if re.match(regex, os.path.split(f)[1])]
  		result= result+findings
  		for find in findings:
  			shutil.copy2(find, os.path.join(output_folder, unicode(number), os.path.split(find)[1]))	
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
	#reading in the spreadsheet
	parser.add_argument("input_file", type=str, help="The input_file is the spreadsheet containing the Gilbert sentence numbers, target forms, etc.")
	initial_args, extras=parser.parse_known_args()
	print initial_args.input_file
	print header, "Running the sentence finder", header
	with open(initial_args.input_file, "r") as inputspread:
		inputdata=pandas.read_csv(inputspread, encoding="utf-8")
	
	#building up criteria	
	for c in inputdata.columns:
		parser.add_argument("--"+c, type=lambda s: unicode(s, 'utf8'))
	parser.add_argument("--move_data", action='store_true', help="If this flag is set, files that match criteria are copied from input_folder to output_folder. input_folder and output_folder are set through graphical interface.")
	parser.add_argument("--output_csv", action='store_true', help="If set, this flag is set, a csv file containing the sentences that match the criteria is written. The output_folder is set through graphical interface.")
	args= parser.parse_args()
	argsdict= vars(args)
	intinput=re.compile(ur"(["+"".join(operatordict.keys())+"]+)(?:\s*?)([0-9]+)", re.UNICODE)
	strinput=re.compile(ur"(["+"".join(operatordict.keys())+"]+)(?:\s*?)(\D)", re.UNICODE)
	outputdata=inputdata
	
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
		output_csv = tkFileDialog.asksaveasfile(mode='w', defaultextension=".csv")
		#output_csv=tkFileDialog.askopenfilename(title="Please choose file name for csv output.")
		outputdata.to_csv(output_csv, encoding="utf-8", index=False)
		print header, "Written csv spreadsheet to {}".format(output_csv)
	if argsdict['move_data']:
		print header, "move_data is activated."
		extracter(outputdata, 'gilbert_number')
	
	
 
#main('/Users/ps22344/Downloads/tgdp-master/summer16/files/gilbert_questions_withtrans_final.csv', 'transcription', 'deːɐ̯', '/Users/ps22344/Downloads/tgdp-master/summer16/files/testsentencefinder.csv')


if __name__ == "__main__":
    main()