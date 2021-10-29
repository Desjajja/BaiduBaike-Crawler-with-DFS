import csv, time, os

def rst2csv(input:list, genre:str='results'):
	cwd = os.getcwd()
	data_path = os.path.join(cwd, 'data')
	if not os.path.exists(data_path):
		os.mkdir(data_path)
	file_path = os.path.join(data_path,'{0}-{1}.csv'.format(genre, time.strftime('%y-%m-%d-%H-%M-%S', time.localtime())))
	try:
		with open(file_path, 'w', encoding='utf-8-sig', newline="") as f:
			fieldnames = list(input[0].keys())
			writer = csv.DictWriter(f, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerows(input)
		print("Succeesfully write {} into the csv file.".format(genre))
	except Exception as e:
		print("Failed to write {} into csv file!!!".format(genre))
		print(e)