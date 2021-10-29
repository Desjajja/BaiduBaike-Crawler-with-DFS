#%%
from bs4 import BeautifulSoup
from urllib import parse
import requests
import re

MAX_DEPTH = 2 # 深度为3

#%%
def urlMatcher(href_tuple:(str, int)) -> str:
	href, dist = href_tuple
	# r = re.compile('(?<=item/).*(?=/)') 
	r = re.compile('(?<=item/).*[^/]') 
	if (dist > 0):
		word = parse.unquote(parse.unquote(r.search(href).group()))
	else:
		word = href
	# item = r.findall(raw) if r.findall(raw) != [] else [raw]
	url = "https://baike.baidu.com/item/{}".format(parse.quote(word))
	return url
#%%
def soupBoiler(url:str):
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' 
	}
	res = requests.get(url, headers = headers)
	res.encoding = 'utf-8'
	html_doc = res.text
	soup = BeautifulSoup(html_doc, 'html.parser')
	return soup



#%%
class DFSNode():
	def __init__(self, url, soup, dist:int):
		# url: full url to parse
		# dist: distance from root node
		self.distance = dist
		self.soup = soup
		self.url = url	# url
		self.title = self.soup.h1.string + self.soup.h2.string if self.soup.h2.attrs == {} else self.soup.h1.string # 词条名称
		self.abstract = re.sub('\[\d*\]','',self.soup.find('div',attrs={"class": "lemma-summary"}).text.replace('\n','').replace('\r','')) # 描述
		self.keyword = self.soup.find('meta', attrs={'name': 'keywords'})['content'] # 关键字信息
		self.hrefs = []

	def getHref(self):
		for tag in set(self.soup.find('div',attrs={"class": "lemma-summary"}).find_all('a', href=True)):
			self.hrefs.append(tag['href'])

