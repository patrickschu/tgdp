import urllib
import os
import requests

# t=unicode("assi")

t='~/Desktop/downi'
directory=os.path.expanduser(t)
print directory
if not os.path.isdir(directory):
	raise IOError("The outputfolder {} is not a valid directory.\nMake sure the folder exists in that place".format(directory))


link="http://www.kick.de/news/fussball/nationalslf/653241/artikel_storck_schwerer-kann-es-auch-nicht-werden.html"
link="http://www.kick.de/news/fussball/nationalslf/653241/artikel_storck_schwerer-kann-es-auch-nicht-werden.html"
resp = requests.head(link)
if resp.status_code != 200:
	raise IOError("The link supplied ({}) does not seem valid (status is {}).\nPlease double-check!".format(link, resp.status_code))