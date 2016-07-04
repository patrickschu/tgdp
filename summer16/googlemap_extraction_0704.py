from bs4 import BeautifulSoup
import codecs
from lxml import etree
import pandas
import numpy.random

places=[]
tree=etree.parse('/Users/ps22344/Downloads/tgdp-master/summer16/TXGDP.kml')
print "root",tree
print type(tree)
print "iter starts here"
for i in tree.getiterator("{http://www.opengis.net/kml/2.2}Placemark"):
 	places.append([r.text for r in i.getchildren()][0])
 	print places
 	
spreadsheet_out=pandas.DataFrame(places)

count=1

sampli=numpy.random.randint(high=3000, low=1000, size=13)
listi=["feature_"+str(num) for num in range(0,10)]

for f in listi:
	spreadsheet_out[f]=sampli+count*100
	count=count+1
	

print  spreadsheet_out
spreadsheet_out.to_csv('gabmap_test.txt', encoding='utf-8', sep='\t', index=False)


g=['feature_1', 'feature_2', 'feature_3', 'feature_4', 'feature_5', 'feature_6', 'feature_7']