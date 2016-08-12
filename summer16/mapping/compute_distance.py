# -*- coding: utf-8 -*-


import scipy
import pandas
import codecs
import numpy as np
from collections import defaultdict
from scipy import spatial

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
		inputspread=outlierremover(inputspread, variable_1, 'oF1', 2)
		inputspread=outlierremover(inputspread, variable_1, 'oF2', 2)
		inputspread=outlierremover(inputspread, variable_2, 'oF1', 2)
		inputspread=outlierremover(inputspread, variable_2, 'oF2', 2)
	#this makes a groupby object
	#below equals inputspread.groupby(inputspread['speaker_number'])
	#split into i, ue here
	print "total length", inputspread.shape
	print "length for '{}' is {}".format(variable_1, inputspread[inputspread['variable']==variable_1].shape)
	print "length for '{}' is {}".format(variable_2, inputspread[inputspread['variable']==variable_2].shape)
	inputspread[inputspread['variable']==variable_1]
	var1dicti=dictmaker(inputspread[inputspread['variable']==variable_1])
	var2dicti=dictmaker(inputspread[inputspread['variable']==variable_2])
	#for entry in var1dicti:
	#	print entry
	#	print var1dicti[entry].get('oF3', None)
	#for entry in var2dicti:
	#	print entry
	#	print var2dicti[entry].get('oF3', None)
	#combine the dictis
	#update var2dicti, i.e. the distance is ue minus i
	for entry in [i for i in var2dicti.keys() if not var1dicti.get(i,None)]:
		print "entry not in the second dict", entry
		var2dicti[entry]['oF3_oF1_distance']="NA"
		var2dicti[entry]['oF2_oF1_distance']="NA"
	for entry in [i for i in var2dicti if var1dicti.get(i,None)]:
		#if var2dicti[entry].get('oF3_oF1_coords', None) and var1dicti[entry].get('oF3_oF1_coords', None):
		#print scipy.spatial.distance.pdist([var2dicti[entry]['oF3_oF1_coords'],var1dicti[entry]['oF3_oF1_coords']], 'euclidean')[0]
		var2dicti[entry]['oF3_oF1_distance']=scipy.spatial.distance.pdist([var2dicti[entry]['oF3_oF1_coords'],var1dicti[entry]['oF3_oF1_coords']], 'euclidean')[0]
		var2dicti[entry]['oF2_oF1_distance']=scipy.spatial.distance.pdist([var2dicti[entry]['oF2_oF1_coords'],var1dicti[entry]['oF2_oF1_coords']], 'euclidean')[0]
		print var2dicti[entry]['oF3_oF1_distance']
	outi=pandas.DataFrame.from_dict(var2dicti, orient='index')
	outi.to_csv('distances.csv')
	
def dictmaker(inputspread):
	"""
	The dictmaker takes a spreadsheet with formant measurements per speaker. Needs to be one vowel only.
	It outputs a dictionary with
	means for F1, F2, F3
	coordinates for (F2, F1), (F3, F1)
	"""
	print "Running the dictmaker"
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
	return speakerdict
#	
#F1 is on y axis
#



distancecomputer('/home/ps/tgdp/summer16/mapping/second_ue_plus_i.csv', 'ʏ', 'ɪ', remove_outliers=False)