#!/usr/bin/python

from bs4 import BeautifulSoup
#from sets import Set
#import Queue
import urllib2
import socket
import threading

num = 0

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


#class parallel(threading.Thread):
#
#  def __init__(self, url):
#
#    threading.Thread.__init__(self)
#    self.url = url
#    self.html = None
#
#  def run(self):
#    print 'start downloading', self.url
#    self.html = download(self.url)
#    print 'end downloading', self.url

def next_month(date):
    year_month = date.split('/')
    year = int(year_month[0])
    month = int(year_month[1])
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
    return str(year) + '/' + str(month).zfill(2)

def en_to_mk(en):
    return en.replace('en_GB','mk')

archive = 'archivelist/setimes/'
base = 'http://setimes.com'

start_date = '2004/09'

socket.setdefaulttimeout(20)

error_log = 'html_error'

ok_log = 'html_ok'



def main ():
    date = start_date
    dates = []
    while (date != '2013/07'):
        dates.append(date)
        date = next_month(date)
    print dates
    while (dates):
        ds = []
        for i in range (0,8):
            if (dates):
                ds.append(dates.pop())
        threads = []
        for d in ds:
            t = threading.Thread(target=get_html, args = (d,'features/'))
            t.daemon = True
            threads.append(t)
            t.start()
        for t in threads:
            t.join()

if __name__ == '__main__':
    main()
