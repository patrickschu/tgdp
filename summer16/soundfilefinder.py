
import codecs
import re
import pandas as pd
import csv
## get numbers of gilbert files
## or read all the shenanigans in here, then make available thru interface


outputfile="gilbert_questions_test.csv"

##read in gilbert
#wordregex="\d+\s\n\s(.*)\n"
wordregex="(\d+)\s\r\s(.*?)\r"
inputfile=codecs.open("//Users/ps22344/Desktop/Questionnaire-1-Gilbert (1)_test_unchaged.txt", "r", "utf-8")
inputtext=inputfile.read()
results=re.findall(wordregex, inputtext)
outputlist=[]
for r in results:
	print r[0],r[1]
	outputlist.append([r[0], r[1]])

columns=['gilbert_number', 'input_form']
print outputlist
dataframe=pd.DataFrame(data=outputlist, columns=columns )
print dataframe
with open(outputfile, "w") as outputi:
    dataframe.to_csv(outputi, encoding="utf-8")
	
