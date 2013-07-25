import re
#import urllib2
import bs4
#import sys
from HTMLParser import HTMLParser
import codecs
#import os

h = HTMLParser()
result = []
############### get content of certain tag = 'target' ##############

def find( element, ok = False):
  change = False
  rez = 0
  for child in element.children:


    if isinstance(child,bs4.element.Tag):
      if child.name == 'table':
        continue
      if child.name == 'div' and child.has_attr('id') and 'id_2' in child['id']:
        print 'end of page found'
        result.append('######')
        continue
      if child.name == 'p':
        ok = True
        change = True

    if isinstance(child,bs4.element.NavigableString):
      if ok == True:
        rez += 1
        result.append(h.unescape(child.output_ready()).encode('utf-8'))

    if hasattr(child,'children'):
      rez += find(child,ok)
      #if (child.name == 'p' or child.name == 'i' or child.name == 'u' or child.name == 'b' or child.name == 'span') and ok:
      #  result.append('#########\n')

    if isinstance(child,bs4.element.Tag) and child.name == 'p':
      result.append('\n')

    if change:
      ok = False
      change = False

  return rez

####################################################################
def splitkeepsep(regex, s):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if is_match(regex, elem) else acc + [elem], re.split(regex, s), [])

def is_match(regex, text):
    pattern = re.compile(regex)
    return pattern.search(text) is not None

# url ex. http://blesok.mk/tekst.asp?lang=mac&tekst=1429&str=1#

#ostatok = int(sys.argv[1])
"""
file = codecs.open('hf',mode='a', encoding='utf-8')
files = os.listdir('mk/')
print files
"""
for x in range(0,1):  # min = 6, max = 1429
  #htmlmk = "3-11 - Ekonomija i monetarna unija.htm"
  htmlen = "mk/1-01 - Politicki kriteriumi.324-487.htm"
  mk = ""
  en = ""
  try:

    html = codecs.open(htmlen,mode='r', encoding='utf-8')
    en = html.read()
    html.close()

  except IOError, err:

    print htmlen + '\tFAILED'
    print 'caught it'
    exit

  except Exception, e:
    print htmlen + '\tUNKNOWN ERROR'
    exit

  #print en
  soup = bs4.BeautifulSoup(en)
  result = []
  body = soup.find('body')
  divs = body.children

  i=0
  for div in divs:
    if isinstance(div,bs4.element.Tag) and div.name == 'div':
      firstp = div.find('p')
      lastp = firstp
      for p in div.findAll('p'):
        lastp = p
      if firstp != None:
        firstp.extract()
        lastp.extract()



  find(soup)
  #print result
  if not result:
    print htmlen + '\t no text found'
    continue
  text = ''.join(result)
  f = open('test', 'w')
  f.write(text)
  f.close()
  pages = text.decode('utf-8').split('######')

  print len(pages)

  while i < len(pages) - 1:
    if pages[i].strip() == '':
      del pages[i]
    elif pages[i+1].strip() == '':
      del pages[i+1]
    elif not re.match('[\.\?!;:]', pages[i].strip()[-1]):
      print pages[i].strip()[-1]
      print pages[i+1].strip()[0]
      if pages[i+1].strip()[0].islower() and not re.match('[a-z]', pages[i+1].strip()[0]) :
        print 'merge'
        pages[i] = pages[i].strip() + ' ' + pages[i+1].strip() + '\n'
        del pages[i+1]
    print i
    i += 1
  text = ''.join(pages)
 # lines = splitkeepsep('\n', text)


  #print result
  #  print text
  filename = 'Politicki Kriteriumi'
  """  j = 0
  for line in lines:
    if line.strip().decode('utf-8').isupper():
      print line
      print '#########'
      j += 1
      """
  f = codecs.open(filename, mode ='a', encoding=('utf-8'))
  f.write(text)
  f.close()



