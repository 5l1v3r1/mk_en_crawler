#!/usr/bin/python


import codecs
import re
#import string
#import threading
import os


def get_sentences(en, i):
    if not (os.path.exists(en) ):
        return
    en_t = codecs.open(en,encoding = 'utf-8',mode ='r')
    l_en = en_t.readline()
    while l_en != '':
        l_en = l_en.replace('\n','').strip()
        s_en = splitkeepsep('([\.\?!:;] )',l_en)
        for s in s_en:
            f = open('SENTENCES/q_' + str(i) + '_en','a')
            f.write(s.encode('utf-8').strip() + '\n')
            f.close()
        l_en = en_t.readline()
#    if l_en != l_mk:
#        f = open('sen_error','a')
#        f.write(str(i) + '\n')
#        f.close()

def splitkeepsep(regex, s):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if is_match(regex, elem) else acc + [elem], re.split(regex, s), [])

def is_match(regex, text):
    pattern = re.compile(regex)
    return pattern.search(text) is not None

def write_list(ss):
    for j in range(0,len(ss)):
        if j == len(ss) - 1:
            print ss[j]
            continue
        if len(ss[j+1]) < 1:
            print ss[j]
            continue
        if ss[j+1][0] == '.':
            print ss[j] + '.'
            j += 1
        elif ss[j+1][0] == '!':
            print ss[j] + '!'
            j += 1
        elif ss[j+1][0] == '?':
            print ss[j] + '?'
            j += 1
        else:
            print ss[j]
def main():
 #   i = 36945
    for j in range (1,18):
        get_sentences('TEXT/q_1_' + str(j) + '_en', j-1)
#    i = 0
#    while i <= 36945:
#        j = i + 8
#        threads = []
#        while i < j:
#            if i > 36945:
#                i += 1
#                continue
#            t = threading.Thread(target=get_sentences, args=('TEXT/text_en_' + str(i), 'TEXT/text_mk_' + str(i), i))
#            t.daemon = True
#            threads.append(t)
#            t.start()
#            i += 1
#        for t in threads:
#            t.join()

if __name__ == '__main__':
    main()
