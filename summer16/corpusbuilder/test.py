# -*- coding: utf-8 -*-

import pandas
import re
import json
import codecs

test="aɪnə"
#test="eine"
print test
variable="ɪ"
print variable
rr= list(test.decode('utf-8'))
print rr
s=rr.index(variable.decode('utf-8'))
print s
pre=rr[s-1]
post=rr[s+1]
print pre, post


# gilbertdata=pandas.read_csv('/Users/ps22344/Downloads/tgdp-master/summer16/files/gilbert_questions_withtrans_final.csv', encoding="utf-8")
# print gilbertdata['id'].dtype
# t=gilbertdata[gilbertdata['gilbert_number']==22]
# print type(t['transcription'])
# print t['transcription'].iloc[0]

# column_dict={
# 'speaker_number':[], 
# 'gilbert_number':[], 
# 'iver_number':[], 
# 'location':[], 
# 'gender':[], 
# 'dob':[]
# }
# for e in column_dict:
# 	column_dict[e].append("assi")
# 	column_dict[e].append("kind")
# t=pandas.DataFrame(column_dict)
# print t
#regex = "(\d+)-(\d+)-(\d+)-(\d+)-(\D+)\.wav"
# thus 
#[0]= iv_number
#[1]= speaker_number
#[2]= ??
#[3]= gilbert_number
#[4] = random alpha character	


# def jsonreader(json_file, fix_formatting_off):
# 	"""
# 	Takes a JSON file with informant data, returns a dictionary with 1 entry per speaker ID. 
# 	Output format: {1: {current_residence: XYZ, speaker_id: XZY, ..},{2:{}}
# 	Repairs faulty JSON formatting if repair_formatting = True; reduces DOB entries to 4 characters. 
# 	Lowercases all string data. 
# 	"""
# 	inputdata=codecs.open(json_file, "r", "utf-8").read()
# 	inputdata=re.findall("\[\{.*\}\]", inputdata)
# 	if len(inputdata) < 1:
# 		raise IOError("Cannot extract the JSON data. Make sure the relevant section starts with '[{' and ends with '}]'.")
# 	inputdata=inputdata[0]
# 	print "Reading JSON data from file '{}'. The file is {} characters long".format(json_file, len(inputdata))
# 	# thank you SO: http://stackoverflow.com/questions/37689400/dealing-with-mis-escaped-characters-in-json
# 	if not fix_formatting_off:
# 		print "Fix formatting on."
# 		inputdata = re.sub(r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'', inputdata)
# 	try: 
# 		jsondata=json.loads(inputdata)
# 	except ValueError, err:
# 		raise ValueError("{} {}".format (err, "\nCannot read the JSON data, try changing the setting for 'fix_formatting'."))
# 	informantdicti={}
# 	count=0
# 	for datapoint in jsondata:
# 		count=count+1
# 		informantdicti[count]={k:v.lower() if isinstance(v,basestring) else v for k,v in datapoint.items() }
# 	for entry in informantdicti:
# 		informantdicti[entry]['DOB']=int(informantdicti[entry]['DOB'].split("-")[0])
# 	return informantdicti
# 
# 
# filis=['1-33-2-3-a.wav', '1-114-2-3-a.wav','7-326-2-3-a.wav', '110-407-2-3-a.wav']
# 
# 
# 
# informantdicti=jsonreader('/Users/ps22344/Desktop/database/informants.json',False)
# 
# def gilbertfileanalyzer(filename, informant_dicti):
# 	"""
# 	The gilbertfileanalyzer takes the name of a Gilbert sound file and a dictionary w/ informant metadata.
# 	It parses the filename to return speaker metadata.
# 	Metadata comes as a list of [speaker_number, gilbert_number, interviewer_number, location, gender, date_of_birth]
# 	"""
# 	print filename
# 	regex='(\d+)-(\d+)-(\d+)-(\d+)-(\D+)\.wav'
# 	res=re.findall(regex,filename)[0]
# 	if len(res) != 5:
# 		raise ValueError("'{}' does not match the pattern for Gilbert files.".format(filename))
# 	iver_number, speaker_number, unknown_thing, gilbert_number, random_character = res
# 		#informant_id is where speaker number lives
# 	meta=[informantdicti[f] for f in informant_dicti if informant_dicti[f].get('informant_id', None) == int(speaker_number)]
# 	
# 	if len(meta) != 1:
# 		raise ValueError("No unambiguous match for speaker ID '{}' extracted out of file '{}'.".format(speaker_number, filename))
# 	
# 	meta=meta[0]
# 	#here we extract metadata to include in the spreadsheet
# 	location, gender, dob = [meta.get('current_residence', None), meta.get('gender', None), meta.get('DOB', None)]
# 	return speaker_number, gilbert_number, iver_number, location, gender, dob
# 	
# 	
# 
# for fili in filis:
# 	r=gilbertfileanalyzer(fili, informantdicti)
# 	print r
# 


# t={'assi':['1','2','3'],
# 'name':['patrick','oberassi','unterassi']
# }
# 
# 
# t2={'assi':['1','2'],
# 'name':['patrick','oberassi']
# }
# 
# full=pandas.DataFrame(t)
# partial=pandas.DataFrame(t2)
# print full
# print partial
# 
# res=pandas.merge(full, partial, how='inner', on='name')
# 
# print "\n\nreulst"
# print  res


#regex=9-134-2-2-a.wav
#regex = "(\d+)-(\d+)-(\d+)-(\d+)-(\D+)\.wav"
# thus 
#[0]= iv_number
#[1]= speaker_number
#[2]= ??
#[3]= gilbert_number
#[4] = random alpha character			
# 