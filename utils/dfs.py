#%%
from bs4 import BeautifulSoup
from urllib import parse
import requests
import re
from cfg import *

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
	def __init__(self, url, soup, dist:int=MAX_DEPTH):
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

#%%
def dfs(seed, depth=MAX_DEPTH) -> tuple:
	results = [] # list of dicts that holds the data
	failures = [] # holds failed urls
	count = 0

	
	stack= [(seed,0)] # original url

	while len(stack) > 0:
		href_tuple = stack.pop(-1) # (url, dist)
		url, dist = href_tuple

		url = urlMatcher(href_tuple)
		soup = soupBoiler(url)
		try:
			node = DFSNode(url, soup, dist)
			node.getHref()
			result = dict(zip(['词条名称','网址', '描述', '关键字'],[node.title, node.url, node.abstract, node.keyword]))
			# results.append((result, node.distance))
			count = count + 1
			if count % 10 == 0:
				print("{} items have been added!".format(count))
			results.append(result)
			if (node.distance < MAX_DEPTH): # if current depth hasn't reach the limit, push its child into the stack
				child_distance = node.distance + 1
				for href in node.hrefs:
					stack.append((href, child_distance))

		except:
			print("Attempt failed: {}".format(url))
			failures.append(url)
			continue
	return (results, failures)