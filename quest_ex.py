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
        if texts[k]['top'] == '1226' or texts[k]['top']== '1225' or texts[k]['top']=='28':
            continue
        if texts[k]['height'] == '23' and texts[k]['font'] == '3' and len(texts[k].getText().strip()) > 3 and texts[k].getText().strip().isupper():
            if not (texts[k-1]['height'] == '23' and texts[k-1]['font'] == '3'):
                j += 1
        text = texts[k].getText()
        if len(text.strip()) < 1:
            if ((k > 0 and len(texts[k-1].findAll('b')) > 0) or
               (k < len(texts) - 1 and len(texts[k+1].findAll('b')) > 0)):
                text = '\n'
            else:
                text = ''
        f = codecs.open('TEXT/q_' + str(i) + '_' + str(j) + '_mk', mode='a', encoding='utf-8')
        f.write(text)
        f.close()

def main():
    parse_text('questionary/3-07 - Zemjodelstvo.xml', 9)

if __name__ == '__main__':
    main()
