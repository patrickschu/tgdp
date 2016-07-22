# -*- coding: utf-8 -*-

import re
import pandas
import os
import codecs

colheaders="File/Spkr\tVowel\tStart\tEnd\tDur\toTime\toPitch\toF1\toF2\toF3\tgTime\tgPitch\tgF1\tgF2\tgF3\tMaxFormants\tNumberPoles\tNotes"
print colheaders
#tools
header="\n\n---\n"
template=""
suffix={
"input_folder":"_vowels.txt",
"input_spread":".wav"
}

#	dob	file_name	gender	gilbert_number	id	input_form	iver_number	location	post_sound	pre_sound	speaker_number	target_form	transcription	variable


#Dataadder output struggles with last line (Notes); sometimes empty, sometimes NA (as it should be), sometimes with values (long files bleed over). 
def dataadder(input_spread, file_name_column, input_folder, cat_to_add="new_column"):
	"""
	The dataadder merges data from the input_folder into the input_spread. 
	It takes a spreadsheet input_spread with metadata, one column of which, named file_name_column, contains file names .
	It adds the measurements contained in files containing the file name and adds them to the spreadsheet. 
	Note that this works with any IDing characteristic. 
	??Do we need cat_to_add??
	"""
	inputspread=pandas.read_csv(input_spread, encoding="utf-8")
	for h in colheaders.rstrip("\n").split("\t"):
		inputspread[h]="NA"
	print len(colheaders.rstrip("\n").split("\t"))
	inputfolder=os.path.expanduser(input_folder)
	inputfilis=[f.decode('utf-8') for f in os.listdir(inputfolder) if f.endswith("_vowels.txt") and not f.startswith(".")]
	print inputfilis	
	for fili in inputfilis:
 		print fili
 		matches= [line for line in inputspread[file_name_column] if re.sub(suffix["input_spread"], suffix["input_folder"], line) == fili]
		if len(matches) == 0:
			print "Nothing found for file '{}' in '{}'".format(fili, input_spread) ,header
			pass
		if len(matches) > 1:
			print header, "Warning! More than one match for file '{}' in '{}'".format(fili, input_spread) ,header
		#investigate: will this break if the files does not exist?
		if len(matches) == 1:
			try:
				filiread=codecs.open(os.path.join(inputfolder, fili), "r", "utf-16").read()
				print 'Length', len(filiread.rstrip("\n").split("\t")), "ought to be '18'"
				inputspread.loc[inputspread[file_name_column]==matches[0], colheaders.rstrip("\n").split("\t")]=filiread.rstrip("\n").split("\t")[:18]
			except UnicodeError, err:
				print "\nUNICODE ISSUE -- FILE {} WAS NOT PROCESSED; probably need to re-create in Praat\n".format(fili), err			
	print header, inputspread
	with open("gilbertsound_125.csv", "w") as outputspread:
		inputspread.to_csv(outputspread, encoding='utf-8', index=False)
	
	
dataadder('/Users/ps22344/Desktop/dataset_rounding/short_ue/125/125.csv', 'id', "/Users/ps22344/Desktop/125_measurements/", 'F1')