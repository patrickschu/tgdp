# -*- coding: utf-8 -*-

import pandas
import os

def spreadmerger(spreadsheet_1, spreadsheet_2, filename=False):
	"""
	The spreadmerger merges a number of spreadsheets into a giant spreadsheet and outputs it as a .csv. 
	The outputspreadsheet's name is a merged version of the inputspreadsheet with the _merged added.
	Watch the axis setting.
	"""
	spreadsheet1=pandas.read_csv(spreadsheet_1, encoding="utf-8")
	spreadsheet2=pandas.read_csv(spreadsheet_2, encoding="utf-8")
	###THIS IS NOT RIGHT, INTRODUCES Nan --> no, the nas are produced by the dataadder
	outputspread=pandas.concat([spreadsheet1,spreadsheet2])
	#check how long a file name may be, construct emergency exit
	#outputspread.to_csv(os.path.join(os.path.split(spreadsheet_1)[1]+os.path.split(spreadsheet_2)[1]+"_merged.csv"), encoding="utf-8", na_rep="NA", index=False, cols=spreadsheet2.columns)
	outputspread.to_csv(os.path.join(os.path.split(spreadsheet_1)[1]+os.path.split(spreadsheet_2)[1]+"_merged.csv"), encoding="utf-8", na_rep="NA", index=False, cols=spreadsheet2.columns)
	print "File written to", os.path.join(os.path.split(spreadsheet_1)[1]+os.path.split(spreadsheet_2)[1]+"_merged.csv")
	return outputspread

spreadmerger('/home/ps/tgdp/summer16/mapping/gilbertsound_1.csvgilbertsound_16.csv_merged.csvgilbertsound_21.csv_merged.csvgilbertsound_111.csv_merged.csvgilbertsound_125.csv_merged.csv', '/home/ps/tgdp/summer16/mapping/shorti_final_FIXED.csv')
