#downloading stuff
#<a href="1-1-1.zip">1-1-1.zip</a><

from bs4 import BeautifulSoup
import urllib
import time


def linkopener(link):
	if not link.startswith("http://"):
 		link="http://"+link
	files_to_download=[]
	inputlink=urllib.urlopen(link).read()
	soup=BeautifulSoup(inputlink, "html.parser")
	for l in [result for result in soup.find_all('a') if result.get('href')]:
		#print l.get('href')
		if l.get('href').endswith(".zip"):
 			print(l.get('href'))
 			files_to_download.append(l.get('href'))
 	for f in files_to_download[:10]:
 		urllib.urlretrieve(link+f, '/Users/ps22344/Desktop/down/'+f)
 		print "File {} downloaded to {}".format(f, "assi")
 		time.sleep(600)
 		print "now sleeping"
 	fullfiles_to_download=[link+f for f in files_to_download]
 	return(fullfiles_to_download)
	
urllib.urlretrieve('http://www.cs.utexas.edu/~eberlein/cs305j/topic3.pdf', '/Users/ps22344/down')







def main(link, directory):
	t=linkopener(link)
	print "here we go", t
	
main("http://dev.laits.utexas.edu/dev_cpittman/tgdp/", "assi")