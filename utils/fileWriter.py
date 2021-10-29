import csv, json, time, os
from cfg import *

def rst2txt(input:list, seed:str, genre:Flag):
	cwd = os.getcwd()
	data_path = os.path.join(cwd, 'data')
	if not os.path.exists(data_path):
		os.mkdir(data_path)
	file_path = os.path.join(data_path,'{0}-{1}-{2}.txt'.format(seed, genre.name, time.strftime('%y-%m-%d-%H-%M-%S', time.localtime())))
	try:
		with open(file_path, 'w', encoding='utf-8') as f:
			for element in input:
				f.write(json.dumps(element, ensure_ascii=False))
				f.write('\n')
		print("Succeesfully write {0}-{1} into the text file.".format(seed, genre.name))
	except Exception as e:
		print("Failed to write {0}-{1} into text file!!!".format(seed, genre.name))
		print(e)

def rst2csv(input:list, seed:str, genre:Flag):
	cwd = os.getcwd()
	data_path = os.path.join(cwd, 'data')
	if not os.path.exists(data_path):
		os.mkdir(data_path)
	file_path = os.path.join(data_path,'{0}-{1}-{2}.csv'.format(seed, genre.name, time.strftime('%y-%m-%d-%H-%M-%S', time.localtime())))
	try:
		with open(file_path, 'w', encoding='utf-8-sig', newline="") as f:
			fieldnames = list(input[0].keys())
			writer = csv.DictWriter(f, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerows(input)
		print("Succeesfully write {0}-{1} into the csv file.".format(seed, genre.name))
	except Exception as e:
		print("Failed to write {0}-{1} into csv file!!!".format(seed, genre.name))
		print(e)


def fileWriter(input, seed, genre:Flag, file_type=FILE_TYPE): 
	if(not genre or file_type == 'txt'):
		rst2txt(input, seed, genre)
	elif (file_type == 'csv'):
		rst2csv(input, seed, genre)
	else:
		print("Invalid File Type! Please check the configuration file.")
