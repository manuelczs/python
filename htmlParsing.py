from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try:
	html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
except HTTPError as e:
	print(e)

bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})

for name in nameList:
	print(name.get_text())
