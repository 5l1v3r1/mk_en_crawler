#!/usr/bin/python

from bs4 import BeautifulSoup
#from sets import Set
#import Queue
import urllib2
import socket


def get_features(date, type):
    print 'http://setimes.com/cocoon/setimes/xhtml/en_GB/archivelist/setimes/'+ type + date
    html = urllib2.urlopen('http://setimes.com/cocoon/setimes/xhtml/en_GB/archivelist/setimes/'+ type + date)
    i = 1
    soup = BeautifulSoup(html)
    divs = soup.findAll('div',{'class':'article'})
    for div in divs:
        for link_tag in div.findAll('a'):
            link = link_tag.get('href')
            link = base + link
            mk_link = en_to_mk(link)
            en_file = open(type[0] + str(i) + '_en', 'w')
            mk_file = open(type[0] + str(i) + '_mk', 'w')
            mk_file.write(urllib2.urlopen(link).read())
            en_file.write(urllib2.urlopen(mk_link).read())
            i += 1



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

start_date = '2004/06'

socket.setdefaulttimeout(20)

def main ():

    date = start_date

    get_features(date, 'features/')

if __name__ == '__main__':
    main()
