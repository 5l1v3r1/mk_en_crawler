#!/usr/bin/python

#from bs4 import BeautifulSoup
#from sets import Set
#import Queue
import urllib2
import socket
import threading



def en_to_mk(en):
    return en.replace('en_GB','mk')

archive = 'archivelist/setimes/'
base = 'http://setimes.com'

start_date = '2004/09'

socket.setdefaulttimeout(10)

error_log = 'links_error'

ok_log = 'links_ok'

def read_link(link, a):
    link = link + a
    global num
    try:
        mk_link = en_to_mk(link)
        en_url = urllib2.urlopen(link).read()
        mk_url = urllib2.urlopen(mk_link).read()
        lock.acquire(1)
        en_file = open('html/' + str(num) + '_en', 'w')
        mk_file = open('html/' + str(num) + '_mk', 'w')
        num += 1
        lock.release()
        en_file.write(en_url)
        mk_file.write(mk_url)
        en_file.close()
        mk_file.close()
        ok = open(ok_log, 'a')
        ok.write(link + '\n')
    except Exception as ex:
        nok = open(error_log, 'a')
        nok.write(str(ex) + '\n')
        nok.write(link + '\n')

num = 0

lock = threading.Lock()

def main ():

    links_f = open('links','r')
    l = links_f.readline()
    links = []
    while (l != ''):
        links.append(l)
        l = links_f.readline()
    while (links):
        ls = []
        for i in range (0,8):
            if (links):
                ls.append(links.pop())
        threads = []
        for link in ls:
            t = threading.Thread(target=read_link, args = (link, ''))
            t.daemon = True
            threads.append(t)
            t.start()
        for t in threads:
            t.join()


if __name__ == '__main__':
    main()
