 # -*- coding: utf-8 -*-

##getting relevant gilbert files
header="\n\n---\n"

import pandas
import argparse
import numpy as np
import operator
import re
import os
import shutil
import Tkinter 
import tkFileDialog


##Note that some gilbert_numbers apply to several sentences. (all up to #20).
def main(inputfile, column, search_term, move_data=True, output_csv=False):
	parser = argparse.ArgumentParser()

	print header, "Running the sentence finder", header
	with open(inputfile, "r") as inputspread:
		inputdata=pandas.read_csv(inputspread, encoding="utf-8")
	for c in inputdata.columns:
		inputname= c
		inputtype= np.dtype(inputdata[c]).type
		#print inputtype
		parser.add_argument("--"+inputname, type=inputtype)	
	
	args= parser.parse_args(['--gilbert_number', '4', '--transcription', 'y'])
	argsdict= vars(args)
	print argsdict
	#i hate that this comes in as a string as opposed to unicode, but seems nothing can be done about it
	for item in [a for a in argsdict if argsdict[a]]:
		if isinstance(argsdict[item], basestring):
			print "Matching {} to '{}'".format(item, argsdict[item])
			outputdata= inputdata[inputdata[item].str.contains(argsdict[item].decode("utf-8"))]
		else:
			print header, "Error: At this point, the sentencefinder does not accept numeric input like '{}'".format(argsdict[item]), header
	print "{} sentences found".format(len(outputdata))
	if output_csv:
		outputdata.to_csv(output_csv, encoding="utf-8", index=False)
		print header, "Written csv spreadsheet to {}".format(output_csv)
	if move_data:
		print header, "Copying data"
		extracter(outputdata, 'gilbert_number')
	
			
			
			
	

	
		

#regex=9-134-2-2-a.wav
#regex = "(\d+)-(\d+)-(\d+)-(\d+)-(\D+)\.wav"
# thus 
#[0]= iv_number
#[1]= speaker_number
#[2]= ??
#[3]= gilbert_number
#[4] = random alpha character			
# 


def extracter(spreadsheet, column_name):
	"""
	extracter moves files
	"""
 	print header, "Running the extracter."
 	root=Tkinter.Tk()
	root.withdraw()
	root.update()
 	input_folder=tkFileDialog.askdirectory(title="Inputfolder: Please choose a directory that contains your corpus files")
 	root=Tkinter.Tk()
	root.withdraw()
	root.update()
 	output_folder=tkFileDialog.askdirectory(title="Outputfolder: Please choose a directory to copy files into")
 	print header, "Copying files from '{}' to '{}'.".format(input_folder, output_folder)
 	#collecting input files
 	inputfiles=[]
 	# for fili in os.walk(input_folder):
# 		files=files+zip(fili[len(fili)-2],fili[len(fili)-1]) 
	print "Locating files."	
	for dirpath, subdirs, files in os.walk(input_folder):
		for f in files:
			inputfiles.append(os.path.join(dirpath, f))
			if len(inputfiles) in [1000,2000,6000,12000,24000]:
				print "{} files processed, still working".format(len(inputfiles))
		

	print "Found {} files".format(len(inputfiles))

 	#read from spreadsheet
 	# with open(spreadsheet, "r") as spreadsheet:
#  		spreadsheet=pandas.read_csv(spreadsheet, encoding="utf-8")
 	numbers_to_be_extracted= spreadsheet[column_name].unique()

 	print header, "Gilbert numbers to be extracted"
 	print ",".join([unicode(i) for i in numbers_to_be_extracted])
 	#finding relevant input files
 	result=[]
	for number in numbers_to_be_extracted:
		print "Processing", number
		regex="(\d+)-(\d+)-(\d+)-"+number.astype('U')+"-(\D+)\.wav"
  		findings= [f for f in inputfiles if re.match(regex, os.path.split(f)[1])]
  		result= result+findings
  		for find in findings:
	   		shutil.copy2(find, os.path.join(output_folder, os.path.split(find)[1]))
  		
  	print header, "{} files have been copied to {}".format(len(result), output_folder)
 	
 	
	
 	# for n in numbers_to_be_extracted:
#  	
#  		print n
# 		
		# we can have one dir, thus listdir
		# subdirs showing up, we need to list as well
		# walk
		#then match filenames to regex
		#copy to outputdir
		#9-134-2-2-a.wav
		#number before a is gilbert_number
		
		
	
#extracter('/Users/ps22344/Downloads/tgdp-master/summer16/files/gilbert_questions_withtrans_final.csv','gilbert_number')
	
	
 
main('/Users/ps22344/Downloads/tgdp-master/summer16/files/gilbert_questions_withtrans_final.csv', 'transcription', 'deːɐ̯', '/Users/ps22344/Downloads/tgdp-master/summer16/files/testsentencefinder.csv')


# if __name__ == "__main__":
#     main()