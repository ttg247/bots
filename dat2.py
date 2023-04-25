import pandas as pd
from google_images_download import google_images_download 
#variables
path = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"

path_1 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_2 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_3 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_4 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_5 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_6 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_7 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_8 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_9 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"
path_10 = "C:\\users\\LAPTOP\\Desktop\\SJ.xlsx"

col = usecols="A"
dtype = dtype="object"

sheet_name_1 = sheet_name="Sheet1"
sheet_name_2 = sheet_name="Sheet2"
sheet_name_3 = sheet_name="Sheet3"
sheet_name_4 = sheet_name="Sheet4" 

#get file
sj_dict = pd.read_excel(path, sheet_name)

#extract data
sj = sj_dict.values.tolist() 

#download images function 
response = google_images_download.googleimagesdownload() 
search_queries = sj
def downloadimages(query): 
	arguments = {"keywords": query, 
				"format": "png", 
				"limit":10, 
				"print_urls":True, 
				"size": "medium", 
				"aspect_ratio":"square"} 
	try: 
		response.download(arguments) 
	 
	except FileNotFoundError: 
		arguments = {"keywords": query, 
					"format": "png", 
					"limit":4, 
					"print_urls":True, 
					"size": "medium"} 
					
		try: 
			response.download(arguments) 
		except: 
			pass  

#load file function
def load(a, b):
	if a == 1:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-one.xlsx" 
	if a == 2:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-two.xlsx"
	if a == 3:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-three.xlsx"
	if a == 4:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-four.xlsx"
	if a == 5:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-five.xlsx"
	if a == 6:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-six.xlsx"
	if a == 7:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-seven.xlsx"
	if a == 8:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-eight.xlsx"
	if a == 9:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-nine.xlsx"
	if a == 10:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\second\\second-ten.xlsx"
	if b == 1:
		sheet_name="Sheet1"
	if b == 2:
		sheet_name="Sheet2"
	if b == 3:
		sheet_name="Sheet3"
	if b == 4:
		sheet_name="Sheet4" 
	sj_dict = pd.read_excel(path, sheet_name, usecols="M",)

	sj = sj_dict.values.tolist()
	for query in sj:  
		downloadimages(query[0])
#done
load(10, 4)

