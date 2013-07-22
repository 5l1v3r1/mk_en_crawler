#!/usr/bin/python


import codecs
#import re
#import string
#import threading
#import os



ends = {}

def get_ends(i):
    try:
        f = codecs.open('SENTENCES/'+ str(i) + '_mk', encoding = 'utf-8', mode = 'r')
    except:
        return
    l = f.readline()
    while l != '':
        try:
            ls = l.split()
            end = ls[len(ls) - 1]
            if end in ends:
                ends[end] += 1
            else:
                ends[end] = 1
        except:
            pass
        l = f.readline()

def main():
    for i in range(0,39646):
        get_ends(i)
    sort_ends = sorted(ends, key=lambda key: -ends[key])
    for e in sort_ends:
        if len(e) <= 2:
            f = codecs.open('ends_mk', mode='a', encoding='utf-8')
            f.write(e + ' ' + str(ends[e]) + '\n')
            f.close()

if __name__ == '__main__':
    main()
