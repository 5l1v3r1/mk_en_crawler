#!/usr/bin/python


import codecs
import re
#import string
import threading
import os


def get_sentences(en, mk, i):
    if not (os.path.exists(en) and os.path.exists(mk)):
        return
    en_t = codecs.open(en,encoding = 'utf-8',mode ='r')
    mk_t = codecs.open(mk,encoding = 'utf-8',mode ='r')
    l_en = en_t.readline()
    l_mk = mk_t.readline()
    while l_en != '' and l_mk != '':
        l_en = l_en.replace('\n','').strip()
        l_mk = l_mk.replace('\n','').strip()
        s_en = splitkeepsep(l_en)
        s_mk = splitkeepsep(l_mk)
#        print l_en + '\n'
        for s in s_en:
            f = open('SENTENCES/' + str(i) + '_en','a')
            f.write(s.encode('utf-8') + '\n')
            f.close()
       # write_list(s_en)
#        print l_mk + '\n'
        for s in s_mk:
            f = open('SENTENCES/' + str(i) + '_mk','a')
            f.write(s.encode('utf-8') + '\n')
            f.close()       # write_list(s_mk)
 #       print str(len(s_en)) + ' ' + str(len(s_mk))
  #      print '\n\n\n'
        l_en = en_t.readline()
        l_mk = mk_t.readline()
    if l_en != l_mk:
        f = open('sen_error','a')
        f.write(str(i) + '\n')
        f.close()

def splitkeepsep(s):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == '. ' or elem == '! ' or elem == '? ' else acc + [elem], re.split('([!\.\?] )', s), [])

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
    i = 0
    while i <= 36945:
        j = i + 8
        threads = []
        while i < j:
            if i > 36945:
                i += 1
                continue
            t = threading.Thread(target=get_sentences, args=('TEXT/text_en_' + str(i), 'TEXT/text_mk_' + str(i), i))
            t.daemon = True
            threads.append(t)
            t.start()
            i += 1
        for t in threads:
            t.join()

if __name__ == '__main__':
    main()
