#-------------------------------------------------------------------------------------------------#
#	DFS implemented Crawler for https://baike.baidu.com/
#-------------------------------------------------------------------------------------------------#
from utils.dfs import *
from utils.fileWriter import *
from cfg import *


status_fail = genre.failed
status_succeed = genre.succeeded


def main():
	seed = input("请输入起始词：")
	suc_list, fail_list = dfs(seed)
	fileWriter(suc_list, seed, status_succeed)
	fileWriter(fail_list, seed, status_fail)

if __name__ == "__main__":
	main()