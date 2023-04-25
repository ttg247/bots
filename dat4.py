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
		path = "C:\\users\\LAPTOP\\Desktop\\partner.xlsx" 
	if b == 1:
		sheet_name="Sheet3"
	sj_dict = pd.read_excel(path, sheet_name, usecols="A",)

	sj = sj_dict.values.tolist()
	for query in sj:  
		downloadimages(query[0])


#execution 
load(1, 1)
# python desktop/py/dat4.py
