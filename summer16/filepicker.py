import json
import os
import codecs
import re
from pprint import pprint

### 
#delete header at beginning
def filepicker(inputfile_json, output_directory, *args):
	data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
	}
	t=json.dumps(data)
	f=json.loads(t)
	print f.keys()
	inputfile=codecs.open(inputfile_json, "r", "utf-8")
	text=inputfile.read()
	newtext=text.replace(r"\'", "'")
	data=json.loads(newtext)
	print data[0]
	count=0
	dicti={}
	for d in data:
		dicti[count]=d
		count=count+1
	print len(dicti)
	print dicti[100]
	
	# outputfile=codecs.open("aaaa.txt", "w", "utf-8")
# 	outputfile.write(newtext)
#   	
# 	t=json.dumps(data)
# 	f=json.loads(t)
# 	print f.keys()
	
	


	# with open(os.path.expanduser(inputfile_json), "r") as f:
# 		input=json.load(f)
		# t=json.dumps(input)
# 		jsonobject=json.loads(t)
# 		print type(jsonobject)



filepicker('/Users/ps22344/Downloads/database/informants.json', 'assi')




















# [{"informant_id": 1,"DOB": "1915-01-01","gender": "M","language_home": "Unknown","language_school": "Unknown","current_residence": "New Braunfels","childhood_residence": "Farm, Rural","education_complete": "Elementary School","created_at": "0000-00-00 00:00:00","updated_at": "2014-11-13 14:15:51","questionnaire": "","is_locked": 1,"island_id": 1}, {"informant_id": 2,"DOB": "1915-01-01","gender": "M","language_home": "Unknown","language_school": "Unknown","current_residence": "New Braunfels","childhood_residence": "Farm, Rural","education_complete": "Unknown","created_at": "0000-00-00 00:00:00","updated_at": "2015-01-27 12:01:57","questionnaire": "{\"interview_id\":\"740094805\",\"upload_status\":\"None\",\"informant_id\":\"2\",\"first_name\":\"\",\"middle_name\":\"\",\"last_name\":\"\",\"gender\":\"M\",\"date_of_birth\":\"1915-01-01\",\"city_of_birth\":\"\",\"state_of_birth\":\"California\",\"country_of_birth\":\"\",\"street_address_of_residence\":\"\",\"city_of_residence\":\"\",\"state_of_residence\":\"--\",\"country_of_residence\":\"\",\"phone_number\":\"\",\"previous_residences\":\"\",\"religious_affiliation_other\":\"\",\"region_in_europe_of_origin\":\"\",\"second_language_age\":\"--\",\"who_taught_second_language\":\"\",\"how_often_child_german_parents\":\"Never\",\"how_often_child_german_parents_comment\":\"\",\"how_often_child_english_parents\":\"Never\",\"how_often_child_english_parents_comment\":\"\",\"how_often_child_german_grandparents_comment\":\"\",\"how_often_child_english_grandparents_comment\":\"\",\"how_often_child_german_teachers_comment\":\"\",\"how_often_child_english_teachers_comment\":\"\",\"how_often_child_german_friends_comment\":\"\",\"how_often_child_english_friends_comment\":\"\",\"how_often_child_german_siblings_comment\":\"\",\"how_often_child_english_siblings_comment\":\"\",\"how_often_child_german_neighbors_comment\":\"\",\"how_often_child_english_neighbors_comment\":\"\",\"how_often_child_german_at_church_comment\":\"\",\"how_often_child_english_at_church_comment\":\"\",\"how_often_child_german_at_school_comment\":\"\",\"how_often_child_english_at_school_comment\":\"\",\"how_often_child_german_at_home_comment\":\"\",\"how_often_child_english_at_home_comment\":\"\",\"how_often_child_german_in_shops_comment\":\"\",\"how_often_child_english_in_shops_comment\":\"\",\"how_often_child_german_at_large_family_gatherings_comment\":\"\",\"how_often_child_english_at_large_family_gatherings_comment\":\"\",\"how_often_child_german_at_other_comment\":\"\",\"how_often_child_english_at_other_comment\":\"\",\"comments_on_childhood_language_use\":\"\",\"how_often_in_1960s_1970s_german_parents_comment\":\"\",\"how_often_in_1960s_1970s_english_parents_comment\":\"\",\"how_often_in_1960s_1970s_german_grandparents_comment\":\"\",\"how_often_in_1960s_1970s_english_grandparents_comment\":\"\",\"how_often_in_1960s_1970s_german_co_workers_comment\":\"\",\"how_often_in_1960s_1970s_english_co_workers_comment\":\"\",\"how_often_in_1960s_1970s_german_friends_comment\":\"\",\"how_often_in_1960s_1970s_english_friends_comment\":\"\",\"how_often_in_1960s_1970s_german_siblings_comment\":\"\",\"how_often_in_1960s_1970s_english_siblings_comment\":\"\",\"how_often_in_1960s_1970s_german_spouse_comment\":\"\",\"how_often_in_1960s_1970s_english_spouse_comment\":\"\",\"how_often_in_1960s_1970s_german_children_comment\":\"\",\"how_often_in_1960s_1970s_english_children_comment\":\"\",\"how_often_in_1960s_1970s_german_neighbors_comment\":\"\",\"how_often_in_1960s_1970s_english_neighbors_comment\":\"\",\"how_often_in_1960s_1970s_german_at_church_comment\":\"\",\"how_often_in_1960s_1970s_english_at_church_comment\":\"\",\"how_often_in_1960s_1970s_german_at_home_comment\":\"\",\"how_often_in_1960s_1970s_english_at_home_comment\":\"\",\"how_often_in_1960s_1970s_german_in_shops_comment\":\"\",\"how_often_in_1960s_1970s_english_in_shops_comment\":\"\",\"how_often_in_1960s_1970s_german_at_large_family_gatherings_comment\":\"\",\"how_often_in_1960s_1970s_english_at_large_family_gatherings_comment\":\"\",\"comments_on_1960s_1970s_language_use\":\"\",\"how_often_currently_german_parents_comment\":\"\",\"how_often_currently_english_parents_comment\":\"\",\"how_often_currently_german_co_workers_comment\":\"\",\"how_often_currently_english_co_workers_comment\":\"\",\"how_often_currently_german_friends_comment\":\"\",\"how_often_currently_english_friends_comment\":\"\",\"how_often_currently_german_siblings_comment\":\"\",\"how_often_currently_english_siblings_comment\":\"\",\"how_often_currently_german_spouse_comment\":\"\",\"how_often_currently_english_spouse_comment\":\"\",\"how_often_currently_german_children_comment\":\"\",\"how_often_currently_english_children_comment\":\"\",\"how_often_currently_german_neighbors_comment\":\"\",\"how_often_currently_english_neighbors_comment\":\"\",\"how_often_currently_german_at_church_comment\":\"\",\"how_often_currently_english_at_church_comment\":\"\",\"how_often_currently_german_at_home_comment\":\"\",\"how_often_currently_english_at_home_comment\":\"\",\"how_often_currently_german_in_shops_comment\":\"\",\"how_often_currently_english_in_shops_comment\":\"\",\"how_often_currently_german_at_large_family_gatherings_comment\":\"\",\"how_often_currently_english_at_large_family_gatherings_comment\":\"\",\"comments_on_people_places\":\"\",\"belong_to_shooting_singing\":\"\",\"which_shooting_singing_clubs\":\"\",\"shooting_singing_clubs_speak_english_comment\":\"\",\"shooting_singing_clubs_speak_german_comment\":\"\",\"comments_shooting_singing_clubs\":\"\",\"other_areas_speak_german\":\"\",\"comments_other_areas_speak_german\":\"\",\"german_spoken_at_school\":\"\",\"comments_german_spoken_at_school\":\"\",\"german_taught_at_school_comment\":\"\",\"german_grammar_taught_at_school_comment\":\"\",\"comments_german_taught_at_school\":\"\",\"high_school_diploma\":\"\",\"study_german_high_school_comment\":\"\",\"college_degree_comment\":\"\",\"study_german_college_comment\":\"\",\"comments_german_studied_at_school\":\"\",\"i_speak_language_1\":\"English\",\"i_speak_language_2\":\"German\",\"i_speak_language_3\":\"\",\"i_speak_language_4\":\"\",\"i_speak_language_5\":\"\",\"i_understand_language_1\":\"English\",\"i_understand_language_2\":\"German\",\"i_understand_language_3\":\"\",\"i_understand_language_4\":\"\",\"i_understand_language_5\":\"\",\"read_german_comment\":\"\",\"write_german_comment\":\"\",\"listen_german_radio_watch_german_tv_comment\":\"\",\"important_texas_german_passed_on_comment\":\"\",\"wish_children_spoke_german_comment\":\"\",\"wish_children_spoke_texas_german_comment\":\"\",\"wish_grandchildren_spoke_german_comment\":\"\",\"wish_grandchildren_spoke_texas_german_comment\":\"\",\"should_texas_german_preserved_comment\":\"\",\"will_texas_german_preserved_comment\":\"\",\"important_texas_german_primary_school_curriculum_comment\":\"\",\"should_german_compulsory_school_comment\":\"\",\"should_texas_german_compulsory_school_comment\":\"\",\"should_regular_radio_texas_german_comment\":\"\",\"should_regular_tv_texas_german_comment\":\"\",\"should_texas_german_road_signs_comment\":\"\",\"identity_rank_german\":\"German\",\"identity_rank_american\":\"American\",\"identity_rank_texan\":\"Texan\",\"identity_rank_american_german\":\"American-German\",\"identity_rank_texas_german\":\"Texas-German\",\"identity_rank_city_county\":\"As a resident of this city or county\",\"comments_why_texas_german_not_spoken\":\"\",\"proud_speaker_texas_german_comment\":\"\",\"texas_german_important_part_identity_comment\":\"\",\"proud_speaker_english_comment\":\"\",\"world_without_texas_german_sad\":\"Sad\",\"world_without_texas_german_possibility\":\"A possibility\",\"world_without_texas_german_richer\":\"Richer\",\"world_without_texas_german_more_modern\":\"More modern\",\"world_without_texas_german_impossible\":\"Impossible\",\"world_without_texas_german_lacking_something\":\"Lacking something\",\"world_without_texas_german_backward\":\"Backward\",\"world_without_texas_german_something_good\":\"Something good\",\"world_without_texas_german_more_practical\":\"More practical\",\"world_without_texas_german_lonely\":\"A lonely place\",\"comments_world_without_texas_german\":\"\",\"associated_with_english_home\":\"Home\",\"associated_with_english_official\":\"Official\",\"associated_with_english_friendly\":\"Friendly\",\"associated_with_english_cozy\":\"Cozy\",\"associated_with_english_foreign\":\"Foreign\",\"associated_with_english_religion\":\"Religion\",\"associated_with_english_arrogant\":\"Arrogant\",\"associated_with_english_rural\":\"Rural\",\"associated_with_english_future\":\"Future\",\"associated_with_english_identity\":\"Identity\",\"associated_with_english_urban\":\"Urban\",\"associated_with_english_love\":\"Love\",\"associated_with_english_hate\":\"Hate\",\"associated_with_english_family\":\"Family\",\"comments_associated_with_english\":\"\"}","is_locked": 0,"island_id": 1},