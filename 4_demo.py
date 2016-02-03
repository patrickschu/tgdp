import re
import os
import codecs

##
directory="/Users/ps22344/Documents/speakers_712"

filelist=[i for i in os.listdir(directory) if not i.startswith(".") ]

#setting up some functions
def tagextractor(text, tag, fili):
	regexstring="<"+tag+"=(.*?)>"
	result=re.findall(regexstring, text, re.DOTALL)
	if len(result) != 1:
		print "alarm in tagextractor", fili, result
	return result[0]
	
def textextractor(text, fili):
	regexstring="<text>(.*?)</text>"
	result=re.findall(regexstring, text, re.DOTALL)
	if len(result) != 1:
		print "alarm in textextractor", fili, result
	return result[0]
	

#MAIN
for fili in filelist:
	filelocation=os.path.join(directory, fili)
	inputread=codecs.open(filelocation, "r", "utf-8")
	inputtext=inputread.read()
	interview=textextractor(inputtext, filelocation)
	speaker=tagextractor(inputtext, "speaker", filelocation)
	wellfinder=re.compile(".{50}\Wwell\W.{50}")
	result=wellfinder.findall(interview.lower())
	print "speaker: ",speaker
	for resi in result:
		print resi, "\t", "speaker: ",speaker
	print "\n------------------\n\n"
		
