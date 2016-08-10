# -*- coding: utf-8 -*-


import scipy
import pandas
import codecs
import numpy as np



#/home/ps/tgdp/summer16/mapping/shortishortue_merged.csv
def outlierremover(spreadsheet, variable, column_name, no_of_stdevs):
	
	#keep NAs in there
	column_mean=np.mean(spreadsheet[spreadsheet['variable']==variable][column_name])
	column_stdev=np.std(spreadsheet[spreadsheet['variable']==variable][column_name])
	#from docs
	# df1.loc[:, df1.loc['a'] > 0]
	print spreadsheet.loc[spreadsheet['variable']==variable]
	print "The mean is {}, the standard deviation is {} for column {}".format(column_mean, column_stdev, column_name)
	#x=t.loc[(t['oF1'] > 700) & (t['variable'] == 'ʏ')]
	outputspread=spreadsheet.loc[(spreadsheet[column_name] > column_mean)]
	print outputspread.describe()
	print outputspread['oF1']
	print "\n\n DIFFERENCE\n before:", spreadsheet.shape, "after", outputspread.shape
	return outputspread

#df.loc[(df["B"] > 50) & (df["C"] == 900), "A"]	
	
	
def distancecomputer(input_file, variable_1, variable_2, remove_outliers=True):
	with codecs.open(input_file, "r", "utf-8") as inputfile:
		inputspread=pandas.read_csv(inputfile)
	#	print help(pandas.DataFrame)
	#	print inputspread
	#	by speaker, compute distance btw i (oF1, oF2) and y (oF1, oF2) in variable
	#print inputspread[inputspread['variable']==variable_2].describe()
	if remove_outliers:
		inputspread=outlierremover(inputspread, variable_1, 'oF1', 2)
		#inputspread=outlierremover(inputspread, variable_1, 'oF2', 2)
		#inputspread=outlierremover(inputspread, variable_2, 'oF1', 2)
		#inputspread=outlierremover(inputspread, variable_2, 'oF2', 2)

	# for speaker in inputspread.groupby(speaker):
		# print speaker
		#make mean F1, F2 of i, make mean F1, F2 of y
		#compute distance





distancecomputer('/home/ps/tgdp/summer16/mapping/shortishortue_merged.csv', 'ʏ', 'ɪ')