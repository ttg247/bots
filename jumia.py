import selenium 
from selenium import webdriver as wb
from selenium.webdriver.support.ui import Select
import pandas as pd 
import time

#opening the browser
wbD = wb.Chrome('downloads/chromedriver/chromedriver.exe')

#running loop to store the product links in a list
listOfLinks = []
condition = True 
while condition:
    time.sleep(3)
    productInfoList = webD.find_elements_by_class_name('a-size-min')
    for el in productInfoList:
        if(el.text !="" and el.text !="Sponsored"):
            pp2 = el.find_element_by_tag_name('a')
            listOfLinks.append(pp2.get_property(href))
    try:
        wbD.find_element_by_class_name('a-last').find_element_by_tag_name('a').get_property('href')
        wbD.find_element_by_class_name('a-last').click()
    except:
        condition = False 
len(listOfLinks)
