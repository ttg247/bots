import pandas as pd
from google_images_download import google_images_download 

#download images function 
response = google_images_download.googleimagesdownload() 

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
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-one.xlsx" 
	if a == 2:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-two.xlsx"
	if a == 3:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-three.xlsx"
	if a == 4:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-four.xlsx"
	if a == 5:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-five.xlsx"
	if a == 6:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-six.xlsx"
	if a == 7:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-seven.xlsx"
	if a == 8:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-eight.xlsx"
	if a == 9:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-nine.xlsx"
	if a == 10:
		path = "C:\\users\\LAPTOP\\Documents\\sj\\third\\third-ten.xlsx"
	if b == 1:
		sheet_name="Sheet1"
	if b == 2:
		sheet_name="Sheet2"
	if b == 3:
		sheet_name="Sheet3"
	if b == 4:
		sheet_name="Sheet4" 
	sj_dict = pd.read_excel(path, sheet_name, usecols="A",)

	sj = sj_dict.values.tolist()
	for query in sj:  
		downloadimages(query[0])


#execution
load(4, 3)

# python desktop/py/dat3.py