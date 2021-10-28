import json
import os
import time
import csv

def rst2txt(input:list, genre:str='results'):
	cwd = os.getcwd()
	data_path = os.path.join(cwd, 'data')
	if not os.path.exists(data_path):
		os.mkdir(data_path)
	file_path = os.path.join(data_path,'{0}-{1}.txt'.format(genre, time.strftime('%y-%m-%d-%H-%M-%S', time.localtime())))
	try:
		with open(file_path, 'w', encoding='utf-8') as f:
			for element in input:
				f.write(json.dumps(element).encode().decode('unicode_escape'))
				f.write('\n')
		print("Succeesfully write {} into the text file.".format(genre))
	except Exception as e:
		print("Failed to write {} into text file!!!".format(genre))
		print(e)

