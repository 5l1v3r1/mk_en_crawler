import re
#import urllib2
#import bs4
#import sys
#from HTMLParser import HTMLParser
import codecs
#import os

filename = 'Politicki Kriteriumi'

f= codecs.open(filename, mode='r',encoding='utf-8')
lines = f.readlines()
j = 0
for line in lines:
  if line.strip().isupper() and re.match('.\..*', line.strip()):
    j += 1
  file = codecs.open(filename + ' ' + str(j),encoding='utf-8', mode = 'a')
  file.write(line)
  file.close()
