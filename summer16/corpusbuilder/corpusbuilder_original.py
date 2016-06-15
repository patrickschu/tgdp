#!/usr/bin/env python

import json
import os
import codecs
import re
import argparse
import sys
import operator
import shutil
from pprint import pprint
import time

##NOTE THAT THIS IS DIFFERENT in PY3

import Tkinter 
import tkFileDialog


#note the speaker regex requires a certain naming pattern. this might be unique. note that only valid for zip and and wav
# if we add additional naming patterns, store them in regexdict
###global variables###

regexdict={
'speaker_regex':"\d+-(\d+)-\d+.zip"
}
speaker_regex="\d+-(\d+)-\d+.*[wav|zip]"
header="\n-----\n"


#the operatordict matches functions to inputstrings
operatordict={
"<":operator.lt,
"<=": operator.le,
"==":operator.eq,
"=":operator.eq,
"!=":operator.ne,
">=":operator.ge,
">":operator.gt
}


###helper functions###
def check_input(*args):
	"""
	Checks if directories supplied as args actually exist
	"""
	for arg in args:
		if not os.path.isdir(arg):
			raise IOError("The directory '{}' can't be found. Make sure it exists at this location.".format(arg))



def jsonreader(json_file, repair_formatting):
	"""
	Takes a JSON file with informant data, returns a dictionary with 1 entry per speaker ID. 
	Output format: {1: {current_residence: XYZ, speaker_id: XZY, ..},{2:{}}
	Repairs faulty JSON formatting if repair_formatting = True; reduces DOB entries to 4 characters. 
	Lowercases all string data. 
	"""
	inputdata=codecs.open(json_file, "r", "utf-8").read()
	inputdata=re.findall("\[\{.*\}\]", inputdata)
	if len(inputdata) < 1:
		raise IOError("Cannot extract the JSON data. Make sure the relevant section starts with '[{' and ends with '}]'.")
	inputdata=inputdata[0]
	print "Reading JSON data from file '{}'. The file is {} characters long".format(json_file, len(inputdata))
	# thank you SO: http://stackoverflow.com/questions/37689400/dealing-with-mis-escaped-characters-in-json
	if repair_formatting:
		print "Repair formatting on."
		inputdata = re.sub(r'(?<!\\)\\(?!["\\/bfnrt]|u[0-9a-fA-F]{4})', r'', inputdata)
	try: 
		jsondata=json.loads(inputdata)
	except ValueError, err:
		raise ValueError("{} {}".format (err, "\nCannot read the JSON data, try setting 'repair_formatting' to 'True'."))
	informantdicti={}
	count=0
	for datapoint in jsondata:
		count=count+1
		informantdicti[count]={k:v.lower() if isinstance(v,basestring) else v for k,v in datapoint.items() }
	for entry in informantdicti:
		informantdicti[entry]['DOB']=int(informantdicti[entry]['DOB'].split("-")[0])
	return informantdicti


def valuegetter(dict, key, operator_string, value):
	"""
	Uses the operation defined in operator_string to match the input value to entries in dict.
	It reads the operators from the operatordict. 
	Prints warning if not value (i.e. dictionary value: None or no parameter (i.e. dictionary lacks key). 
	Returns matches in resultlist, errors in no_value and no_key. 
	"""
	if not operatordict.get(operator_string, None):
		raise TypeError("The operator '{}', supplied with the parameter '{}', is not valid\n". format(operator_string, key))
	else:
		operator=operatordict[operator_string]
		results={i:dict[i] for i in dict if operator(dict[i].get(key, None),value)}
		
		no_value={i for i in dict if dict[i].get(key)==None}
		if no_value:
			print "There are no values for this parameter in these files: ", [str(i) for i in no_value]
		no_key={i for i in dict if key not in dict[i].keys()}
		if no_key:
			print "There is no such category in these files: ", [str(i) for i in no_key]
		return results, no_value, no_key



###MAIN####

def main():

	##inputting JSON
	print header, "Running the corpusbuilder."
	print "Please choose JSON file containing informant metadata."
	root=Tkinter.Tk()
	root.withdraw()
	root.update()
	json_file=tkFileDialog.askopenfilename(title="Please choose JSON file containing informant metadata")
	informantdicti=jsonreader(json_file, repair_formatting=True)
	#collect keys, i.e. possible input 
	keys=[v.keys() for k,v in informantdicti.items()]
	keys=[item for listi in keys for item in listi]
	#informantdicti[0]={'gender':None, 'DOB':1999}
	keys=list(set(keys))
		

	#set up input arguments
	parser = argparse.ArgumentParser()
	for key in keys:
		parser.add_argument("--"+key, type=str, help="Possible input to the argument '{}' includes: {:.1500} ".format(key, ", ".join(set([str(informantdicti[e].get(key)) for e in informantdicti]))))
	args = parser.parse_args()
	argsdict=vars(args)
	if set(argsdict.values()) == set([None]):
		print "Warning: You did not enter any conditions to select data. Use the '--help' command to see your options."
	
	
	
	#setting up in and out
	
	print "Please choose a directory that contains your corpus files"
	root=Tkinter.Tk()
	root.withdraw()
	##inputdir manually. only for lazy people
	inputdir=[os.path.expanduser(os.path.join("~/Desktop/gilli", str(i))) for i in range(1,149)]
	#inputdir = [tkFileDialog.askdirectory(title="Inputfolder: Please choose a directory that contains your corpus files")]
	print "Please choose a directory to copy files into."
	root=Tkinter.Tk()
	root.withdraw()
	root.update()
	outputdir = tkFileDialog.askdirectory(title="Outputfolder: Please choose a directory to copy files into")
	print "{}'{}' set as input folder".format(header, ", ".join(inputdir))
	print "'{}' set as output folder {}".format(outputdir, header)
	check_input(outputdir,*inputdir)
	inputfilis=[]
	for dir in inputdir:
		inputfilis.append([i for i in os.listdir(dir) if re.match(speaker_regex, i)])
	inputfilis=[item for listi in inputfilis for item in listi]
	print len(inputfilis)
	#iterate over all arguments, collect in resultlist
	resultlist=[]
	for entry in [e for e in argsdict if argsdict[e] and e in keys]:
		intinput=re.compile("(["+"".join(operatordict.keys())+"]+)(?:\s*?)([0-9]+)")
		strinput=re.compile("(["+"".join(operatordict.keys())+"]+)(?:\s*?)([a-z]+)")
		if re.match(strinput, argsdict[entry].lower()):
			#what if they try to use > or < with a string
			matcher=re.findall(strinput, argsdict[entry].lower())[0]
			print "Matching ", entry, " ".join(matcher)
			results, no_value, no_key = valuegetter(informantdicti, entry, matcher[0], str(matcher[1]))	
			resultlist.append(results)
		elif re.match(intinput, argsdict[entry]):
			matcher=re.findall(intinput, argsdict[entry])[0]
			print "Matching ", entry, " ".join(matcher)
			results, no_value, no_key = valuegetter(informantdicti, entry, matcher[0], int(matcher[1]))
			resultlist.append(results)
		else:
			print "\nError: No match for the input ", entry
	#note that resultlist contains the dictionary keys, which are numbers != speaker_ids
	resultlist_keys=[i.keys() for i in resultlist]
	sharedresultlist=set.intersection(*[set(i) for i in resultlist_keys])
	print "{}{} speakers meet the criteria:".format(header, len(sharedresultlist))
	sharedresultspeakers=[str(informantdicti[i]["informant_id"]) for i in sharedresultlist]
	print "IDs {}".format(", ".join(sharedresultspeakers))
	for speaker_id in sharedresultspeakers:
		speaker_entry={k:v for k,v in informantdicti.items() if v.get("informant_id") == int(speaker_id)}
		
		json.dump(speaker_entry, file(os.path.join(outputdir,"speaker"+speaker_id+".txt"), 'w'))
		#switch back on for basic input
		#files_to_copy=[i for i in inputfilis if re.findall(speaker_regex, i)[0] == speaker_id]
		for dir in inputdir:
			#print os.listdir(dir)
			all_files=[i for i in os.listdir(dir) if re.match(speaker_regex, i)]
			files_to_copy=[i for i in all_files if re.findall(speaker_regex, i)[0] == speaker_id]
			print speaker_id, files_to_copy		
			if len(files_to_copy) > 0:
				for fili in files_to_copy:
					shutil.copy2(os.path.join(dir, fili), os.path.join(outputdir,fili))
					print "Copied '{}' to '{}'".format(os.path.join(dir, fili), os.path.join(outputdir,fili))
			# else:
# 				print "There are no files associated with speaker ID {} in location '{}'`".format(speaker_id, inputdir)
		
	print header, "Corpus builder exited."



if __name__ == "__main__":
    main()













# [{"informant_id": 1,"DOB": "1915-01-01","gender": "M","language_home": "Unknown","language_school": "Unknown","current_residence": "New Braunfels","childhood_residence": "Farm, Rural","education_complete": "Elementary School","created_at": "0000-00-00 00:00:00","updated_at": "2014-11-13 14:15:51","questionnaire": "","is_locked": 1,"island_id": 1}, {"informant_id": 2,"DOB": "1915-01-01","gender": "M","language_home": "Unknown","language_school": "Unknown","current_residence": "New Braunfels","childhood_residence": "Farm, Rural","education_complete": "Unknown","created_at": "0000-00-00 00:00:00","updated_at": "2015-01-27 12:01:57","questionnaire": "{\"interview_id\":\"740094805\",\"upload_status\":\"None\",\"informant_id\":\"2\",\"first_name\":\"\",\"middle_name\":\"\",\"last_name\":\"\",\"gender\":\"M\",\"date_of_birth\":\"1915-01-01\",\"city_of_birth\":\"\",\"state_of_birth\":\"California\",\"country_of_birth\":\"\",\"street_address_of_residence\":\"\",\"city_of_residence\":\"\",\"state_of_residence\":\"--\",\"country_of_residence\":\"\",\"phone_number\":\"\",\"previous_residences\":\"\",\"religious_affiliation_other\":\"\",\"region_in_europe_of_origin\":\"\",\"second_language_age\":\"--\",\"who_taught_second_language\":\"\",\"how_often_child_german_parents\":\"Never\",\"how_often_child_german_parents_comment\":\"\",\"how_often_child_english_parents\":\"Never\",\"how_often_child_english_parents_comment\":\"\",\"how_often_child_german_grandparents_comment\":\"\",\"how_often_child_english_grandparents_comment\":\"\",\"how_often_child_german_teachers_comment\":\"\",\"how_often_child_english_teachers_comment\":\"\",\"how_often_child_german_friends_comment\":\"\",\"how_often_child_english_friends_comment\":\"\",\"how_often_child_german_siblings_comment\":\"\",\"how_often_child_english_siblings_comment\":\"\",\"how_often_child_german_neighbors_comment\":\"\",\"how_often_child_english_neighbors_comment\":\"\",\"how_often_child_german_at_church_comment\":\"\",\"how_often_child_english_at_church_comment\":\"\",\"how_often_child_german_at_school_comment\":\"\",\"how_often_child_english_at_school_comment\":\"\",\"how_often_child_german_at_home_comment\":\"\",\"how_often_child_english_at_home_comment\":\"\",\"how_often_child_german_in_shops_comment\":\"\",\"how_often_child_english_in_shops_comment\":\"\",\"how_often_child_german_at_large_family_gatherings_comment\":\"\",\"how_often_child_english_at_large_family_gatherings_comment\":\"\",\"how_often_child_german_at_other_comment\":\"\",\"how_often_child_english_at_other_comment\":\"\",\"comments_on_childhood_language_use\":\"\",\"how_often_in_1960s_1970s_german_parents_comment\":\"\",\"how_often_in_1960s_1970s_english_parents_comment\":\"\",\"how_often_in_1960s_1970s_german_grandparents_comment\":\"\",\"how_often_in_1960s_1970s_english_grandparents_comment\":\"\",\"how_often_in_1960s_1970s_german_co_workers_comment\":\"\",\"how_often_in_1960s_1970s_english_co_workers_comment\":\"\",\"how_often_in_1960s_1970s_german_friends_comment\":\"\",\"how_often_in_1960s_1970s_english_friends_comment\":\"\",\"how_often_in_1960s_1970s_german_siblings_comment\":\"\",\"how_often_in_1960s_1970s_english_siblings_comment\":\"\",\"how_often_in_1960s_1970s_german_spouse_comment\":\"\",\"how_often_in_1960s_1970s_english_spouse_comment\":\"\",\"how_often_in_1960s_1970s_german_children_comment\":\"\",\"how_often_in_1960s_1970s_english_children_comment\":\"\",\"how_often_in_1960s_1970s_german_neighbors_comment\":\"\",\"how_often_in_1960s_1970s_english_neighbors_comment\":\"\",\"how_often_in_1960s_1970s_german_at_church_comment\":\"\",\"how_often_in_1960s_1970s_english_at_church_comment\":\"\",\"how_often_in_1960s_1970s_german_at_home_comment\":\"\",\"how_often_in_1960s_1970s_english_at_home_comment\":\"\",\"how_often_in_1960s_1970s_german_in_shops_comment\":\"\",\"how_often_in_1960s_1970s_english_in_shops_comment\":\"\",\"how_often_in_1960s_1970s_german_at_large_family_gatherings_comment\":\"\",\"how_often_in_1960s_1970s_english_at_large_family_gatherings_comment\":\"\",\"comments_on_1960s_1970s_language_use\":\"\",\"how_often_currently_german_parents_comment\":\"\",\"how_often_currently_english_parents_comment\":\"\",\"how_often_currently_german_co_workers_comment\":\"\",\"how_often_currently_english_co_workers_comment\":\"\",\"how_often_currently_german_friends_comment\":\"\",\"how_often_currently_english_friends_comment\":\"\",\"how_often_currently_german_siblings_comment\":\"\",\"how_often_currently_english_siblings_comment\":\"\",\"how_often_currently_german_spouse_comment\":\"\",\"how_often_currently_english_spouse_comment\":\"\",\"how_often_currently_german_children_comment\":\"\",\"how_often_currently_english_children_comment\":\"\",\"how_often_currently_german_neighbors_comment\":\"\",\"how_often_currently_english_neighbors_comment\":\"\",\"how_often_currently_german_at_church_comment\":\"\",\"how_often_currently_english_at_church_comment\":\"\",\"how_often_currently_german_at_home_comment\":\"\",\"how_often_currently_english_at_home_comment\":\"\",\"how_often_currently_german_in_shops_comment\":\"\",\"how_often_currently_english_in_shops_comment\":\"\",\"how_often_currently_german_at_large_family_gatherings_comment\":\"\",\"how_often_currently_english_at_large_family_gatherings_comment\":\"\",\"comments_on_people_places\":\"\",\"belong_to_shooting_singing\":\"\",\"which_shooting_singing_clubs\":\"\",\"shooting_singing_clubs_speak_english_comment\":\"\",\"shooting_singing_clubs_speak_german_comment\":\"\",\"comments_shooting_singing_clubs\":\"\",\"other_areas_speak_german\":\"\",\"comments_other_areas_speak_german\":\"\",\"german_spoken_at_school\":\"\",\"comments_german_spoken_at_school\":\"\",\"german_taught_at_school_comment\":\"\",\"german_grammar_taught_at_school_comment\":\"\",\"comments_german_taught_at_school\":\"\",\"high_school_diploma\":\"\",\"study_german_high_school_comment\":\"\",\"college_degree_comment\":\"\",\"study_german_college_comment\":\"\",\"comments_german_studied_at_school\":\"\",\"i_speak_language_1\":\"English\",\"i_speak_language_2\":\"German\",\"i_speak_language_3\":\"\",\"i_speak_language_4\":\"\",\"i_speak_language_5\":\"\",\"i_understand_language_1\":\"English\",\"i_understand_language_2\":\"German\",\"i_understand_language_3\":\"\",\"i_understand_language_4\":\"\",\"i_understand_language_5\":\"\",\"read_german_comment\":\"\",\"write_german_comment\":\"\",\"listen_german_radio_watch_german_tv_comment\":\"\",\"important_texas_german_passed_on_comment\":\"\",\"wish_children_spoke_german_comment\":\"\",\"wish_children_spoke_texas_german_comment\":\"\",\"wish_grandchildren_spoke_german_comment\":\"\",\"wish_grandchildren_spoke_texas_german_comment\":\"\",\"should_texas_german_preserved_comment\":\"\",\"will_texas_german_preserved_comment\":\"\",\"important_texas_german_primary_school_curriculum_comment\":\"\",\"should_german_compulsory_school_comment\":\"\",\"should_texas_german_compulsory_school_comment\":\"\",\"should_regular_radio_texas_german_comment\":\"\",\"should_regular_tv_texas_german_comment\":\"\",\"should_texas_german_road_signs_comment\":\"\",\"identity_rank_german\":\"German\",\"identity_rank_american\":\"American\",\"identity_rank_texan\":\"Texan\",\"identity_rank_american_german\":\"American-German\",\"identity_rank_texas_german\":\"Texas-German\",\"identity_rank_city_county\":\"As a resident of this city or county\",\"comments_why_texas_german_not_spoken\":\"\",\"proud_speaker_texas_german_comment\":\"\",\"texas_german_important_part_identity_comment\":\"\",\"proud_speaker_english_comment\":\"\",\"world_without_texas_german_sad\":\"Sad\",\"world_without_texas_german_possibility\":\"A possibility\",\"world_without_texas_german_richer\":\"Richer\",\"world_without_texas_german_more_modern\":\"More modern\",\"world_without_texas_german_impossible\":\"Impossible\",\"world_without_texas_german_lacking_something\":\"Lacking something\",\"world_without_texas_german_backward\":\"Backward\",\"world_without_texas_german_something_good\":\"Something good\",\"world_without_texas_german_more_practical\":\"More practical\",\"world_without_texas_german_lonely\":\"A lonely place\",\"comments_world_without_texas_german\":\"\",\"associated_with_english_home\":\"Home\",\"associated_with_english_official\":\"Official\",\"associated_with_english_friendly\":\"Friendly\",\"associated_with_english_cozy\":\"Cozy\",\"associated_with_english_foreign\":\"Foreign\",\"associated_with_english_religion\":\"Religion\",\"associated_with_english_arrogant\":\"Arrogant\",\"associated_with_english_rural\":\"Rural\",\"associated_with_english_future\":\"Future\",\"associated_with_english_identity\":\"Identity\",\"associated_with_english_urban\":\"Urban\",\"associated_with_english_love\":\"Love\",\"associated_with_english_hate\":\"Hate\",\"associated_with_english_family\":\"Family\",\"comments_associated_with_english\":\"\"}","is_locked": 0,"island_id": 1},