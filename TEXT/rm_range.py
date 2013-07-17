#!/usr/bin/python

import os

def main():
    for i in range(15000,15200):
        try:
            os.remove('text_en_' + str(i))
            os.remove('text_mk_' + str(i))
        except:
            continue

if __name__ == '__main__':
    main()
