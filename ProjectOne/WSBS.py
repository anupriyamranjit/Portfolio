# -*- coding: utf-8 -*-
import bs4 as bs
import urllib.request
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time




browser = webdriver.Chrome(executable_path=r'/Users/Anu/Desktop/chromedriver')
url = u'https://twitter.com/BarackObama'
browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for i in range(13):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

tweets = browser.find_elements_by_class_name('tweet-text')
source = browser.page_source
soup = bs.BeautifulSoup(source,'lxml')

def get_handle(BSobject):
    for handle in BSobject.find_all('a', class_='ProfileHeaderCard-screennameLink u-linkComplex js-nav'):
        for at in handle.find_all('b', class_='u-linkComplex-target'):
            print(at.text)
    return(at.text)


obamatweet = []
for m in tweets:
    obamatweet.append(m.text)
data_transposed = zip(obamatweet)
df = pd.DataFrame(data_transposed, columns=["Tweet"])
print(df.head())

df.to_csv('OBAMATWITTER.csv')
