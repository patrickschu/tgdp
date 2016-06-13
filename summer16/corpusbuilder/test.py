import urllib
import os
import requests
import Tkinter
import tkFileDialog
import sys
import argparse

# t=unicode("assi")
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
# 	raise IOError("The link supplied ({}) does not seem valid (status is {}).\nPlease double-check!".format(link, resp.status_code))

# root=Tkinter.Tk()
# root.withdraw()
# json_file=tkFileDialog.askopenfile(title="Please choose the JSON file containing the informant metadata")

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--repair_formatting', default=False, help='Fixes mis-formatted JSON files. Accepted input: True or False')
	args = parser.parse_args()
	print args
# 	if repair_formatting == 'on':
#  		print "repair is an"
# 	if repair_formatting == 'off':
# 		print "repair is ausgeknippst"
# 	else:
# 		print "bs input"
		
if __name__ == "__main__":
    main()