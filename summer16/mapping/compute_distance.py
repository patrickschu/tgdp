# -*- coding: utf-8 -*-


import scipy
import pandas
import codecs
import numpy as np
from collections import defaultdict


#/home/ps/tgdp/summer16/mapping/shortishortue_merged.csv
def outlierremover(spreadsheet, variable, column_name, no_of_stdevs):
	#keep NAs in there
	#this is unfinished
	print "Removing outliers {} stdevs from the mean".format(no_of_stdevs)
	column_mean=np.mean(spreadsheet[spreadsheet['variable']==variable][column_name])
	column_stdev=np.std(spreadsheet[spreadsheet['variable']==variable][column_name])
	#from docs
	# df1.loc[:, df1.loc['a'] > 0]
	print spreadsheet.loc[spreadsheet['variable']==variable]
	print "The mean is {}, the standard deviation is {} for column {}".format(column_mean, column_stdev, column_name)
	#x=t.loc[(t['oF1'] > 700) & (t['variable'] == 'ʏ')]
	outputspread=spreadsheet.loc[((spreadsheet[column_name] > column_mean-(no_of_stdevs*column_stdev))&(spreadsheet[column_name] < column_mean+(no_of_stdevs*column_stdev)))|(spreadsheet['variable'] != variable)]
	print outputspread.describe()
	print outputspread['oF1']
	print "\n\n DIFFERENCE\n before:", spreadsheet.shape, "after", outputspread.shape
	outputspread.to_csv("CSVSCSV.csv")
	return outputspread

#df.loc[(df["B"] > 50) & (df["C"] == 900), "A"]	
	
	
def distancecomputer(input_file, variable_1, variable_2, remove_outliers=True):

	with codecs.open(input_file, "r", "utf-8") as inputfile:
		inputspread=pandas.read_csv(inputfile)
	if remove_outliers:
		inputspread=outlierremover(inputspread, variable_1, 'oF1', 1)
		inputspread=outlierremover(inputspread, variable_1, 'oF2', 2)
		inputspread=outlierremover(inputspread, variable_2, 'oF1', 2)
		inputspread=outlierremover(inputspread, variable_2, 'oF2', 2)
	#this makes a groupby object
	#below equals inputspread.groupby(inputspread['speaker_number'])
	#split into i, ue here
	var1dicti=dictmaker(variable_1)
	var2dicti=dictmaker(variable_2)
	

	
def dictmaker(inputspread):
	"""
	The dictmaker takes a spreadsheet with formant measurements per speaker.
	It outputs a dictionary with
	means for F1, F2, F3
	coordinates for (F2, F1), (F3, F1)
	"""
	speakerdict=defaultdict()
	t=inputspread.groupby('speaker_number')
	#we convert the k[1] dataframe into a dictionary
	speakerdict={k[0]:k[1].to_dict(orient='list') for k in t}
	for entry in speakerdict:
		for f in ['oF1', 'oF2', 'oF3']:
			speakerdict[entry][f]=[np.float64(i) for i in  speakerdict[entry][f]]
			speakerdict[entry][f+"_mean"]=np.mean([i for i in speakerdict[entry][f] if not np.isnan(i)])
		speakerdict[entry]['oF2_oF1_coords']=(speakerdict[entry]['oF2_mean'], speakerdict[entry]['oF1_mean'])
		speakerdict[entry]['oF3_oF1_coords']=(speakerdict[entry]['oF3_mean'], speakerdict[entry]['oF1_mean'])
		for g in ['speaker_number', 'gender']:
		#we might want to use set here if this gets expanded. for now, easier this way.
			if len(set(speakerdict[entry][g])) > 1:
				print "WARNING: MORE THAN ONE '{}' IN HERE".format(g)
			speakerdict[entry][g]=speakerdict[entry][g][0]

outi=pandas.DataFrame.from_dict(speakerdict, orient='index')	
#F1 is on y axis
#

#print outi
outi.to_csv("test.csv")	
	
#print t.sum()
#
#t.to_csv("test.csv")
#this sseems terribly inelegant
#for speaker in inputspread['speaker_number']:
#	print speaker
#	speakerdict[speaker]['f1']=inputspread[inputspread['speaker_number']==speaker]['oF1']
#	speakerdict[speaker]['f2']=inputspread[inputspread['speaker_number']==speaker]['oF2']
#print speakerdict

#inputspread.groupby(
# for speaker in inputspread.groupby(speaker):
	# print speaker
	#make mean F1, F2 of i, make mean F1, F2 of y
	#compute distance
	#also for f1 , f3 




distancecomputer('/home/ps/tgdp/summer16/mapping/shorti_final_FIXED.csvshortue_final_FIXED.csv_merged.csv', 'ʏ', 'ɪ', remove_outliers=False)