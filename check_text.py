#!/usr/bin/python

#import bs4
#import codecs
#import re
#import string
#import threading
import os.path

def check_text(en, mk,i):
    if not os.path.isfile(en) or not os.path.isfile(mk):
        f = open('text_error', 'a')
        f.write(str(i) + '\n')
        f.close()

def main():
    for i in range(0,36946):
        check_text('TEXT/text_en_' + str(i),'TEXT/text_mk_' + str(i), i)

if __name__ == '__main__':
    main()
