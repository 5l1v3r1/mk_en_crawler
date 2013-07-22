#!/usr/bin/python

#import bs4
#import codecs
#import re
#import string
#import threading

def check_text(en, mk,i):
    html_en = open(en).read()
    html_mk = open(mk).read()
    if len(html_en) < 100 or len(html_mk) < 100:
        f = open('parse_error', 'a')
        f.write(str(i) + '\n')
        f.close()

def main():
    for i in range(0,36946):
        check_text('HTML/' + str(i) + '_en','HTML/' + str(i) + '_mk', i)

if __name__ == '__main__':
    main()
