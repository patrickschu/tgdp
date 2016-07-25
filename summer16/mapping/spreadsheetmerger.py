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
	outputspread.to_csv(os.path.join(os.path.split(spreadsheet_1)[1]+os.path.split(spreadsheet_2)[1]+"_merged.csv"), encoding="utf-8", na_rep="NA", index=False, cols=spreadsheet2.columns)
	print "File written to", os.path.join(os.path.split(spreadsheet_1)[1]+os.path.split(spreadsheet_2)[1]+"_merged.csv")
	return outputspread

spreadmerger('/Users/ps22344/Downloads/tgdp/summer16/gilberttools/gilbertsound_74_shorti.csv', '/Users/ps22344/Downloads/tgdp/summer16/gilberttools/gilbertsound_125_shorti.csv' )
