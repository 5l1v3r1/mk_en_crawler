import re
#import urllib2
#import bs4
#import sys
#from HTMLParser import HTMLParser
import codecs
import os

files = os.listdir('text/')
files = [f for f in files if not re.match('^1\-01.*', f)]
files.sort()
print files

for filename in files:
  f= codecs.open('text/' + filename, mode='r',encoding='utf-8')
  lines = f.readlines()
  j = 0
  for line in lines:
    if line.strip().isupper() and re.match('^[IVX]+[\.\ ].*', line.strip()):
      j += 1
    file = codecs.open('text/' + filename + '-' + str(j),encoding='utf-8', mode = 'a')
    file.write(line)
    file.close()

