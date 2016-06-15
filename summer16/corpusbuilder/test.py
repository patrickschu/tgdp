import json
import argparse

# import urllib
# import os
# import requests
# 
# # t=unicode("assi")
# 
# t='~/Desktop/downi'
# directory=os.path.expanduser(t)
# print directory
# if not os.path.isdir(directory):
# 	raise IOError("The outputfolder {} is not a valid directory.\nMake sure the folder exists in that place".format(directory))
# 
# 
# link="http://www.kick.de/news/fussball/nationalslf/653241/artikel_storck_schwerer-kann-es-auch-nicht-werden.html"
# link="http://www.kick.de/news/fussball/nationalslf/653241/artikel_storck_schwerer-kann-es-auch-nicht-werden.html"
# resp = requests.head(link)
# if resp.status_code != 200:
# 	raise IOError("The link supplied ({}) does not seem valid (status is {}).\nPlease double-check!".format(link", "resp.status_code))


# t={69: {u'current_residence': u'comfort'", "u'is_locked': 0", "u'gender': u'm'", "u'created_at': u'0000-00-00 00:00:00'", "u'updated_at': u'0000-00-00 00:00:00'", "u'childhood_residence': u'farm", "rural'", "u'island_id': 1", "u'DOB': 0", "u'informant_id': 70", "u'language_school': u'unknown'", "u'education_complete': u'unknown'", "u'questionnaire': u''", "u'language_home': u'unknown'}}
# 
# json.dump(t", "file('testttttttttt.txt'", "'w'))

# tt=[1,2,3,2]
# r=[i for i in tt if i == 10]
# print r


# 
def main():
    	parser = argparse.ArgumentParser()
     	subparsers = parser.add_subparsers(help='sub-command help')
      	settingsparser = subparsers.add_parser('settings') #i want a subparser called 'settings'
      	settingsparser.add_argument('--fix_formatting', action='store_true') #this subparser shall have a --fix_formatting

#Then I try to parse only the "settings" part like so:
      	
      	settings=parser.parse_args(['settings'])
      	print settings
      	
#This seems to work. But then I add my other keys and things break: 

    	keys=['alpha','beta','gamma','delta']
    	for key in keys:
    		parser.add_argument("--"+key, type=str, help="X")
    	print parser
    	args = parser.parse_args(['--alpha test'])
    	print args
	
main()

# #resi=["doss", "floresville", "universal city, 
#                         "sisterdall", "columbus", "frelsburg/fayetteville",   "sisterdale", "kirby", "fredericksburg"", "wharton", "hamilton",  "solms", "giddings", "hamilton county", "garden ridge,  converse", "boerne", "8 mile creek", "comal co.", " giddings", "goliad co.", "wimberly", "olfem","pittsburgh", "pa", "ranch east of fredericksburg","bulverde", "freyburg/black jack", "mason", "cave creek","gill. co.", "columbus", "kirby", "castroville", "cave creek", "frelsburg", "stonewall", "wimberly", "texas", "doss", "dripping springs", "conroe", "warda", "wall", "cat spring", "clifton", "miles", "lee county", "lagrange", schulenburg", "new braunfels", "waldeck", "between wall & san angelo", "fisher", "hamilton county, luckenbach", "la grange", "freyburg", "converse", "gidings, mcqueeny", "spring branch", "san angelo", "houston, cherry springs", "geronimo", "new braunfels", "san marcos", "serbin", "winchester", "mcgregor", "comal county", "offen", "comfort", "san antonio", "fr", "marion", "mission valley", "midland", "freyburg/schulenburg, victoria", "seguin", "rio medina", "wall", "leroy, bracken", "warrenton", "round top", "cedar park", "freyburg", "comal co.]