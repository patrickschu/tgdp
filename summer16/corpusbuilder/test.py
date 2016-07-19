# -*- coding: utf-8 -*-


import pandas
import sys
import re

# perioddicti={'ala':[1,2,3], 'bussi':[100,200,300]}
# rr={'col1': ['2', '2', '4'], 'filename':['5-1.txt', u'2-1.txt', '1-1.txt'] , 'col3':['pre', 'pre1', 'pre2']}
# 
# ff=pandas.DataFrame(rr)
# print ff, "\n\n\n\n"
# 
# 
# ff['extracol']=[1,2,3]
# 
# print ff
# #print ff[ff['rcol1']=='pre1']
# 
# # tt=pandas.DataFrame(perioddicti)
# # print tt


inputfilis=[u'3-1.txt', u'2-1.txt', '1-1.txt'] 
inputspread=pandas.DataFrame({'col1': ['2', '2', '4'], 'filename':['5-1.txt', u'2-1.txt', '1-1.txt'] , 'col3':['pre', 'pre1', 'pre2']})
inputspread['alli']="na"

print inputspread
for fili in inputfilis:
	print fili, "\n"
	matches= [line for line in inputspread['filename'] if line == fili]
	if matches:
		t=matches[0]
		inputspread.loc[inputspread['filename']==t, 'alli']="ASSSSSSSSI"
print inputspread

