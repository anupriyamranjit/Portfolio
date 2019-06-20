# -*- coding: utf-8 -*-
import bs4 as bs
import urllib.request
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




browser = webdriver.Chrome(executable_path=r'/Users/anupriyamranjit/Downloads/chromedriver')
url = u'https://uwflow.com/course/spcom100'
browser.get(url)
time.sleep(0)

body = browser.find_element_by_tag_name('body')

for i in range(0):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0)

profname = browser.find_elements_by_class_name('prof-name')
rating = browser.find_elements_by_class_name('num-ratings')
percentage = browser.find_elements_by_class_name('rating')
source = browser.page_source
soup = bs.BeautifulSoup(source,'lxml')



profnamelist = []
for m in profname :
    profnamelist.append(m.text)

ratinglist = []
for n in rating:
    ratinglist.append(n.text)

percentagelist = []
for z in percentage:
    percentagelist.append(z.text)







data_transposed1 = list(zip(profnamelist,ratinglist,percentagelist))

df = pd.DataFrame(data_transposed1, columns=["Prof Name","Number of People","Rating Number"])
print(df.head())

df.to_csv('SPCOM100Prof.csv')
