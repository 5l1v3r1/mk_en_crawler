#!/usr/bin/python

import bs4
import codecs
#import re
#import string
import threading

def parse_text(en, mk,i):
    html_en = open(en).read()
    html_mk = open(mk).read()
    if len(html_en) < 100 or len(html_mk) < 100:
        print str(i) + ' NOK'
        return
    en_soup = bs4.BeautifulSoup(html_en)
    mk_soup = bs4.BeautifulSoup(html_mk)
    try:
        en_paras = en_soup.find('div',{'class':'article'}).children
        mk_paras = mk_soup.find('div',{'class':'article'}).children
    except:
        f = open('parse_error','a')
        f.write(str(i) + '\n')
        f.close()
        return
    for p in en_paras:
        if isinstance(p,bs4.element.Tag) and p.name == 'p':
            en_text = p.getText().replace('\n', ' ')
#            if verify_text (en_text, mk_text):
            try:
                f_en = codecs.open('TEXT/text_en_' + str(i), encoding='utf-8', mode='a')
                f_en.write(en_text + '\n')
                f_en.close()
#                print str(i) + ' OK'
            except:
                f = open('parse_error','a')
                f.write(str(i) + '\n')
                f.close()
                continue
    for p in mk_paras:
        if isinstance(p,bs4.element.Tag) and p.name == 'p':
            mk_text = p.getText().replace('\n', ' ')
#            if verify_text (en_text, mk_text):
            try:
                f_mk = codecs.open('TEXT/text_mk_' + str(i), encoding='utf-8', mode='a')
                f_mk.write(mk_text + '\n')
                f_mk.close()
#                print str(i) + ' OK'
            except:
                f = open('parse_error','a')
                f.write(str(i) + '\n')
                f.close()
                continue
#            else:
#                try:
#                    f_en = codecs.open('texts2/error_en_' + str(i), encoding='utf-8', mode='a')
#                    f_mk = codecs.open('texts2/error_mk_' + str(i),encoding='utf-8', mode='a')
#                    f_en.write(en_text + '\n')
#                    f_mk.write(mk_text + '\n')
#                    f_en.close()
#                    f_mk.close()
#                except:
#                    continue

#def verify_mk(text):
#    words_list = re.sub('['+string.punctuation+']', '', text).split()
#    words = set(words_list)
#    count = 0
#    for word in words:
#        if word in mk_words:
#            count += 1
#    if 2*count < len(words):
#        return False
#    else:
#        return True

def verify_text(en,mk):
    if len(en) < 20 or len(mk) < 20:
        return False
    if len(mk) > 1.5*len(en):
        return False
    if len(en) > 1.5*len(mk):
        return False
#    if en in paragraphs:
#        return False
#    else:
#        paragraphs.add(en)
#    if not verify_mk(mk):
#        return False
    return True

#def init_mk_words():
#    global mk_words
#    f = codecs.open('wfl-mk.tbl', encoding='utf-8', mode='r')
#    l = f.readline()
#    while l != '':
#        mk_words.add(l.split()[0])
#        l = f.readline()

#mk_words = set()
#paragraphs = set()

def main():
#    init_mk_words()
    i = 15000
    while i <= 15199:
        j = i + 8
        threads = []
        while i < j:
            if i > 15199:
                i += 1
                continue
            t = threading.Thread(target=parse_text, args=('HTML/' + str(i) + '_en','HTML/' + str(i) + '_mk', i))
            t.daemon = True
            threads.append(t)
            t.start()
            i += 1
        for t in threads:
            t.join()

if __name__ == '__main__':
    main()
