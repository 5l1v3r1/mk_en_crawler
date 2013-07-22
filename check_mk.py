#!/usr/bin/python

import string
import codecs
import re
import os

def init_mk_words():
    global mk_words
    f = codecs.open('wfl-mk.tbl', encoding='utf-8', mode='r')
    l = f.readline()
    while l != '':
        mk_words.add(l.split()[0])
        l = f.readline()

def verify_mk(text):
    text.replace('\n', ' ')
    words_list = re.sub('['+string.punctuation+']', '', text).split()
    words = set(words_list)
    count = 0
    for word in words:
        if word in mk_words:
            count += 1
    if 2*count < len(words):
        return False
    else:
        return True

mk_words = set()


def main():
    init_mk_words()
    for i in range(0,36946):
        try:
            f = codecs.open('TEXT/text_mk_' + str(i), encoding = 'utf-8', mode = 'r')
        except:
            continue
        text = f.read()
        if not verify_mk(text):
            try:
                rem = codecs.open('rem_' +str(i), encoding='utf-8', mode='w')
                rem.write(text)
                rem.close()
                os.remove('TEXT/text_mk_' + str(i))
                os.remove('TEXT/text_en_' + str(i))
            except:
                continue

if __name__ == '__main__':
    main()

