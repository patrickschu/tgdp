# -*- coding: utf-8 -*-
			#split
			
			#count in dict
		
# 	iterate over spreadsheet['filenumber'] to build dicti for this time period
# 	investigate dicti i.e count and log for hapax, total words
# 	
# 	what about plurals etc
# 	output spreadsheet['period','wordcount','hapax', 'ment_hapax']
	

d={u'the': {1760: 449681, 1730: 167622, 1700: 167413, 1770: 703317, 1740: 208781, 1710: 250601, 1780: 863036, 1750: 323117, 1720: 131804, 1790: 730562},
u'of': {1760: 317218, 1730: 113233, 1700: 97417, 1770: 433029, 1740: 135417, 1710: 164958, 1780: 562792, 1750: 224721, 1720: 79000, 1790: 470691},
u'and': {1760: 236790, 1730: 93551, 1700: 89576, 1770: 310855, 1740: 140494, 1710: 139683, 1780: 432216, 1750: 190621, 1720: 80319, 1790: 365702}}


overallhapax={k:v for k,v in d.items() if sum(v.values()) == 1}
print overallhapax	
# 	
# import re
# from collections import defaultdict
# 
# t=defaultdict(dict)
# print t
# 
# text="I have the ugly dog by my side and my side by"
# for period in [1800,1900, 2000]:
# 	p=defaultdict(list)
# 	for item in text.split():
# 		p[item].append(item)
# 	print p
# 	for entry in p:
# 		print type(t[entry])
# 		print t[entry]
# 		t[entry][period]=len(p[entry])
# 
# print t
# 
# #dicti={'he':{1900:10, 2000:1}  'she':

# 
# perioddicti={'ala':10, 'bussi':1}
# #print {k:v for k:v in perioddicti if v ==1}
# t={k:v for k,v in perioddicti.items() if v == 1}
# print t
# 
# t=re.sub(r"('s|s|s's|ed)\b", "", "the")
# print t

# import nltk
# 
# from nltk.corpus import stopwords
# stop=stopwords.words('english')
# 
# 
# def remover(original_list, to_delete):
# 	newlist=[s for s in original_list if s not in to_delete]
# 	return newlist
	


# #PRONOUNS
# perspronouns=[u'i', u'me', u'we', u'you', u'he', u'him',  u'she', u'her', u'it', u'they', 'them',  u'myself', u'ourselves',  u'yourself', u'yourselves',  u'himself',  u'herself', u'itself', u'themselves', u'who', u'whom']
# 
# dempronouns=[u'that', u'these', u'those']
# 
# pospronouns=[u'my', u'our', u'ours', u'your', u'yours', u'his', u'her', u'hers',u'its',  u'their', u'theirs' ]
# 
# 
# #VERBS
# beverb=[u'am', u'is', u'are', u'was', u'were', u'be', u'been', u'being', u'isn', u'wasn', u'weren', u'won', u'ain', u'aren', u're', u'm', u's']
# 
# haveverb=[u'have', u'has', u'had', u'having', u'hadn', u'hasn', u'haven', u've', u'd']
# 
# doverb=[u'do', u'does', u'did', u'doing', u'didn', u'doesn', u'don']
# 
# modals=[u'mightn', u'mustn', u'needn', u'shan', u'shouldn',  u'wouldn',  u'couldn', u'should',u'can']
# 
# negation=[u'mightn', u'mustn', u'needn', u'shan', u'shouldn',  u'wouldn',  u'couldn', u'no', u'nor', u'not', u't']
# 
# aux=[u'll', u'will']
# 
# #MISC
# prepsandarts=[u'of', u'at', u'by', u'for', u'with', u'about', u'against', u'between', u'into', u'through', u'during', u'before', u'after', u'above', u'below', u'to', u'from', u'up', u'down', u'in', u'out', u'on', u'off', u'over', u'under', u'a', u'an', u'the']
# 
# conjuncts=[u'and', u'but', u'if', u'or', u'because', u'as', u'until', u'while']
# 
# adverbsandadjects=['again', u'further', u'then', u'once', u'here', u'there', u u'when', u'where', u'why', u'how', u'all', u'any', u'what', u'which',  u'this'] 
# 
# intensifiers=[u'few', u'more', u'most', u'too', u'very', u'than'
# 
# questions=[u'when', u'where', u'why', u'how']
# 
# leftovers=[u'all', u'any', u'both', u'each',u'other', u'some', u'such', u'only', u'own', u'same', u'so', u'just', u'now', u'o', u'y', u'ma']
# 
# t=remover(stop, pronouns+pospronouns+preps+beverb+haveverb+doverb)
# print t
# 
# 
# 
# 
# 


# test="aɪnə"
# #test="eine"
# print test
# variable="ɪ"
# print variable
# rr= list(test.decode('utf-8'))
# print rr
# s=rr.index(variable.decode('utf-8'))
# print s
# pre=rr[s-1]
# post=rr[s+1]
# print pre, post


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