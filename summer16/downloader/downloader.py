#downloading stuff
#<a href="1-1-1.zip">1-1-1.zip</a><

from bs4 import BeautifulSoup
import urllib
import time
import os
import requests
import sys

def main(link, directory):
	"""
	The downloader downloads zip-files from a web site to a specified folder.
	Returns a list containing the files names of the files found. 
	Arguments:
	link -- needs to be a URL of the format "http://xy.z", pointing to a web site containing .zip files. 
	directory -- an existing folder, this is where the files will be downloaded to
	"""
	#catching errors
	directory=os.path.expanduser(str(directory))
	if not os.path.isdir(directory):
		raise IOError("{} is not a valid directory. Make sure the folder exists at that location".format(directory))
	if not link.startswith("http://"):
 		link="http://"+link
	if requests.head(link).status_code != 200:
		raise IOError("The link supplied ({}) does not seem valid (status is {}).\nPlease double-check!".format(link, resp.status_code))
	files_to_download=[]
	inputlink=urllib.urlopen(link).read()
	soup=BeautifulSoup(inputlink, "html.parser")
	for l in [result for result in soup.find_all('a') if result.get('href')]:
		#print l.get('href')
		if l.get('href').endswith(".zip"):
 			#print(l.get('href'))
 			files_to_download.append(l.get('href'))
 	if len(files_to_download) > 0:
 		print "{} files to be downloaded".format(len(files_to_download))
 	 	for f in files_to_download:
			urllib.urlretrieve(link+f, os.path.join(directory,f))
			print "File {} downloaded to {}".format(f, directory)
			time.sleep(20)
	else:
		print "No .zip files found on this web site. Double-check the link supplied."
 	result=[link+f for f in files_to_download]
 	print "\nDownloader exited.\n"
 	return(result)


if __name__ == "__main__":
    main(*sys.argv[1:])
