#-------------------------------------------------------------------------------------------------#
#	DFS implemented Crawler for https://baike.baidu.com/
#-------------------------------------------------------------------------------------------------#
from utils.parser import *
from utils.rst2txt import rst2txt
from utils.rst2csv import rst2csv

def main():
	results = [] # list of dicts that holds the data
	failures = [] # holds failed urls
	seed = input("请输入起始词：")
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
	rst2csv(results)
	rst2txt(failures, genre='failures')

if __name__ == "__main__":
	main()