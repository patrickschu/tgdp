# -*- coding: utf-8 -*-



def spreadmerger(spreadsheet_1, spreadsheet_2, filename=False):
	"""
	The spreadmerger merges a number of spreadsheets into a giant spreadsheet and outputs it as a .csv. 
	The outputspreadsheet's name is a merged version of the inputspreadsheet with the _merged added.
	"""
	spreadsheet1=pandas.read_csv(spreadsheet_1, encoding="utf-8")
	spreadsheet2=pandas.read_csv(spreadsheet_2, encoding="utf-8")
	outputspread=pandas.concat([spreadsheet1,spreadsheet2], axis=1)
	print os.path.split(spreadsheet_1)
	outputspread.to_csv(os.path.join(otadir, "outputfiles", os.path.split(spreadsheet_1)[1]+os.path.split(spreadsheet_2)[1]+"_merged.csv"), encoding="utf-8")
	return outputspread

spreadmerger('/Users/ps22344/Downloads/ota/outputfiles/hapaxes_25yearperiods_overall_13_50_07_21.csv', '/Users/ps22344/Downloads/ota/outputfiles/hapaxes_25yearperiods_ment_13_39_07_21.csv' )
