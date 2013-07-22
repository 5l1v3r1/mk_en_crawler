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
        s_en = splitkeepsep('([\.\?!:;] )',l_en)
        s_mk = splitkeepsep('([\.\?!:;] )',l_mk)
#        print l_en + '\n'
        for j in range(0,len(s_en)):
            final = s_en[j].strip()
            if final == '***' or len(final) < 1:
                continue
            f = codecs.open('SENTENCES/' + str(i) + '_en',mode='a', encoding='utf-8')
            if check_ends_en(final, s_en, j):
                f.write(final + ' ')
            else:
                f.write(final + '\n')
            f.close()
       # write_list(s_en)
#        print l_mk + '\n'
        for j in range(0,len(s_mk)):
            final = s_mk[j].strip()
            if final == '***' or len(final) < 1:
                continue
            f = codecs.open('SENTENCES/' + str(i) + '_mk',mode='a', encoding='utf-8')
            if check_ends_mk(final, s_mk, j):
                f.write(final + ' ')
            else:
                f.write(final + '\n')
            f.close()       # write_list(s_mk)
 #       print str(len(s_en)) + ' ' + str(len(s_mk))
  #      print '\n\n\n'
        l_en = en_t.readline()
        l_mk = mk_t.readline()
    if l_en != l_mk:
        f = open('sen_error','a')
        f.write(str(i) + '\n')
        f.close()

def splitkeepsep(regex, s):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if is_match(regex, elem) else acc + [elem], re.split(regex, s), [])

def is_match(regex, text):
    pattern = re.compile(regex)
    return pattern.search(text) is not None

def init_ends():
    en = codecs.open('ends', encoding='utf-8', mode='r')
    mk = codecs.open('ends_mk', encoding='utf-8', mode='r')
    l = en.readline()
    while l != '':
        ends_en.add(l.strip())
        l = en.readline()
    l = mk.readline()
    while l != '':
        ends_mk.add(l.strip())
        l = mk.readline()

def check_ends_en(final, s_en, i):
    sp = final.split()
    if sp[-1] in ends_en:
        #f = codecs.open('ends_check_en',mode='a', encoding='utf-8')
        if i+1 < len(s_en):# and s_mk[i+1][0].islower():
            #f.write(final + ' ' + s_en[i+1].strip() + '\n')
            return True
    return False

def check_ends_mk(final, s_mk, i):
    sp = final.split()
    if sp[-1] in ends_mk:
        #f = codecs.open('ends_check_mk',mode='a', encoding='utf-8')
        if i+1 < len(s_mk):# and s_mk[i+1][0].islower():
        #    f.write(final + ' ' + s_mk[i+1].strip() + '\n')
            return True
    if sp[-1] in nums:
        #f = codecs.open('ends_check_mk',mode='a', encoding='utf-8')
        if i+1 < len(s_mk) and s_mk[i+1][0].islower():
           # f.write(final + ' ' + s_mk[i+1].strip() + '\n')
            return True
    return False
ends_mk = set()
ends_en = set()
nums = {'0.','1.', '2.', '3.', '4.','5.','6.','7.','8.','9.'}

def main():
    init_ends()
    print ends_en
    print ends_mk
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
