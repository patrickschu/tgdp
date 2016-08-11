# -*- coding: utf-8 -*-


import scipy
import pandas
import codecs
import numpy as np
from collections import defaultdict


#/home/ps/tgdp/summer16/mapping/shortishortue_merged.csv
def outlierremover(spreadsheet, variable, column_name, no_of_stdevs):
	#keep NAs in there
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
	speakerdict=defaultdict(dict)
	with codecs.open(input_file, "r", "utf-8") as inputfile:
		inputspread=pandas.read_csv(inputfile)
	if remove_outliers:
		inputspread=outlierremover(inputspread, variable_1, 'oF1', 1)
		inputspread=outlierremover(inputspread, variable_1, 'oF2', 2)
		inputspread=outlierremover(inputspread, variable_2, 'oF1', 2)
		inputspread=outlierremover(inputspread, variable_2, 'oF2', 2)
	#this makes a groupby object
	#below equals inputspread.groupby(inputspread['speaker_number'])
	t=inputspread.groupby('speaker_number')
	for i in t:
		#i[0] contains the speaker number, the i[1] is the data associated with it
		print i[0]
		print "F1s",  i[1]['oF1']
		print "mean", i[1]['oF1'].mean()
		print "mean", i[1]['oF1'].count()

		
		
		
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