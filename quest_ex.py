#!/usr/bin/python

import bs4
import codecs
#import re
#import string
#import threading

def parse_text(xml, i):
    soup = bs4.BeautifulSoup(open(xml,'r').read())
    texts = soup.findAll('text')
    j = 0
    for k in range(0,len(texts)):
        if texts[k]['top'] == '31' or texts[k]['top'] == '1226':
            continue
        if texts[k]['height'] == '19' and len(texts[k].getText()) > 3:
            j += 1
        text = texts[k].getText()
        if len(text) < 3:
            if len(texts[k-1].findAll('b')) + len(texts[k+1].findAll('b')) > 0:
                text = '\n'
            else:
                text = ''
        f = codecs.open('TEXT/q_' + str(i) + '_' + str(j) + '_en', mode='a', encoding='utf-8')
        f.write(text)
        f.close()

def main():
    parse_text('questionary/1-01 - Political Criteria.xml', 1)

if __name__ == '__main__':
    main()
