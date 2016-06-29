 # -*- coding: utf-8 -*-


#getting transcripts for gilbert table
from bs4 import BeautifulSoup
import urllib
import codecs
import pandas as pd
import requests
import json

header="\n\n---\n"
##note the encoding nightmare in here

def transcriber(inputfile, outputfile, column, json_file=None):
	"""
	The transcriber adds a column of IPA transcriptions and entry lengths to a spreadsheet.
	Inputfile is a csv file; outputfile a new csv file; column is the column name of the column to be transcribed.
	The optional json_file takes a dictionary of format {word1:IPA_transcription, word2:...}.
	Words not found in the dictionary are looked up online and added to the dictionary.
	The transcriber outputs the csv file with columns 'transcription' and 'items' (# of words) added. 
	It also writes the final version of the word:IPA dictionary into a JSON file called outputfile + '_dict.txt'.
	"""
	
	print "Transcriber started"
	my_dicti={}
	if json_file:
		print header, "Reading JSON file from ", json_file
		json_input=codecs.open(json_file, "r", "utf-8")
		my_dicti=json.load(json_input)
	print "Dictionary entries: ", len(my_dicti)
	inputfile=pd.read_csv(inputfile, encoding="utf-8")
	print header, inputfile[column], header
	transcriptions=[]
	length=[]
	for line in inputfile[column]:
		entry=line.split(" ")
		entry_transcription=[]
		for word in entry:
			print header, word
			if my_dicti.get(word, None) == None:
				transcription=wiktionaryfinder(word)
				print "Looking {} up online".format(word)
				entry_transcription.append(transcription)
				my_dicti[word]=transcription
			else:
				print "Found {} in my_dicti".format(word)
				transcription=my_dicti[word]
				entry_transcription.append(transcription)
		print entry_transcription
		print [type(i) for i in entry_transcription]
		transcriptions.append(" ".join(entry_transcription))
		length.append(len(entry_transcription))
		with open(outputfile+"_dicti.txt", "w") as dictiwriter:
			json.dump(my_dicti, dictiwriter)
	inputfile['transcription']=transcriptions	
	inputfile['items']=length
	with open(outputfile, "w") as outputfile:
		inputfile.to_csv(outputfile, encoding="utf-8")
	print header, inputfile, header
	
	print header, "Transcriber exited, files written to ", outputfile, "+ _dicti"
	
		





#helper functions	

def wiktionaryfinder(inputword):
	"""
	The wiktionaryfinder looks up the input word on Wiktionary and returns a IPA transcription of the word.
	It then extracts all IPA transcriptions on the relevant page.
	If there is more than one, it asks for user input. 
	If there is not Wiktionary page for the input word, it asks the user to input a transcription.
	""" 
	inputword=umlautchecker(inputword)
	inputword=capschecker(inputword)
	link="https://de.wiktionary.org/wiki/"+inputword
	link=link.encode('utf-8')
	inputi=urllib.urlopen(link).read()
	inputisoup=BeautifulSoup(inputi, 'html.parser')	
	results= [r.string for r in inputisoup.find_all('span', 'ipa') if r.string and not r.string.startswith("-")]
	if len(results) == 0:
		print "No options found. Please enter transcription for", inputword
		final_form=raw_input("Which form do you want?\n")
	if len(results) ==1 :
		final_form=results[0]
	if len(results) > 1:
		print "Several options found for word", inputword
		for result in results:
			print result
		final_form=raw_input("Which form do you want?\n")
 	return final_form
	


def capschecker(inputword):
	"""
	The capschecker tests whether a lowercase word exists on Wiktionary. 
	If not, it capitalizes the word and re-tests.
	Returns whatever is working, and inputword if nothing does. 
	"""
	
	link="https://de.wiktionary.org/wiki/"+inputword
	link=link.encode('utf-8')
	originalstatus=requests.get(link)
	if originalstatus.status_code in [404]:
		newlink="https://de.wiktionary.org/wiki/"+inputword.capitalize()
		newlink=newlink.encode('utf-8')
		newstatus=requests.get(newlink)
		if newstatus.status_code not in [404]:
			print inputword, "has been changed to", inputword.capitalize(), "by the capschecker"
			return inputword.capitalize()
		else:
			return inputword
	else:
		print "Capschecker didn't change a thing"
		return inputword


	
def umlautchecker(inputword):
	"""
	The umlautchecker replaces all ae, oe and ue strings with the respective umlaut characters. 
	Note that the dictionary can be expanded quite easily.
	"""
	umlautdict={
	'ae': 'ä',
	'ue': 'ü',
	'oe': 'ö'
	}
	for item in umlautdict.keys():
		inputword=inputword.replace(item, umlautdict[item].decode('utf-8'))
	return inputword
	
	
	
	
	
transcriber('/Users/ps22344/Downloads/tgdp-master/summer16/gilbert_questions.csv', '/Users/ps22344/Downloads/tgdp-master/summer16/gilbert_questions_withtrans_2ndtry.csv', 'target_form', '/Users/ps22344/Downloads/tgdp-master/summer16/gilbert_questions_withtrans_2ndtry.csv_dicti.txt')


