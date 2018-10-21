from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

#html = urlopen('http://www.pythonscraping.com/pages/page1.html')

def getTitle(url):
  # first try get url
  try:
    html = urlopen(url)
  except HTTPError as e:
    return None
  try:
    bsObj = BeautifulSoup(html.read())
    title = bsObj.body.h1
  except AtributeError as e:
    return None
  return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')

if title == None:
  print('Title not found!')
else:
  print(title)
