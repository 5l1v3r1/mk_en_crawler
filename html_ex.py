#!/usr/bin/python

from bs4 import BeautifulSoup
#from sets import Set
#import Queue
import urllib2
import socket
import threading



def get_html(date, type):
    global lock
    global num
    for d in range(1,32):
        try:
            url = 'http://setimes.com/cocoon/setimes/xhtml/en_GB/archivelist/setimes/'+ type + date + '/' + str(d).zfill(2)
            html = urllib2.urlopen(url)
        except:
            e = open(error_log, 'a')
            e.write('no entries:' + url + '\n')
            e.close()
            continue
        soup = BeautifulSoup(html)
        divs = soup.findAll('div',{'class':'article'})
        for div in divs:
            for link_tag in div.findAll('a'):
                link = link_tag.get('href')
                link = base + link
                #mk_link = en_to_mk(link)
                f = open('links', 'a')
                f.write(link + '\n')
                f.close()
#                try :
#                    en_file = open('html/' + type[0] + '_' + str(num) + '_en', 'w')
#                    mk_file = open('html/' + type[0] + '_' + str(num) + '_mk', 'w')
#                    en_file.write(urllib2.urlopen(link).read())
#                    mk_file.write(urllib2.urlopen(mk_link).read())
#                    en_file.close()
#                    mk_file.close()
#                    ok = open(ok_log, 'a')
#                    ok.write(link + '\n')
#                    num += 1
#                except Exception as ex:
#                    e = open(error_log, 'a')
#                    e.write(str(ex) + '\n')
#                    e.write('error: ' + link + '\n')
#                    e.close()

def en_to_mk(en):
    return en.replace('en_GB','mk')

archive = 'archivelist/setimes/'
base = 'http://setimes.com'

start_date = '2004/09'

socket.setdefaulttimeout(20)

error_log = 'links_error'

ok_log = 'links_ok'

def read_link(link, a):
    link = link + a
    global num
    try:
        mk_link = en_to_mk(link)
        en_file = open('html/' + str(num) + '_en', 'w')
        mk_file = open('html/' + str(num) + '_mk', 'w')
        en_file.write(urllib2.urlopen(link).read())
        mk_file.write(urllib2.urlopen(mk_link).read())
        en_file.close()
        mk_file.close()
        ok = open(ok_log, 'a')
        ok.write(link + '\n')
        num += 1
    except Exception as ex:
        nok = open(error_log, 'a')
        nok.write(str(ex) + '\n')
        nok.write(link + '\n')

num = 0

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
