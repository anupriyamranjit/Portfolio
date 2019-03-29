# -*- coding: utf-8 -*-
import bs4 as bs
import urllib.request
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



browser = webdriver.Chrome(executable_path=r'/Users/Anu/Desktop/chromedriver')
url = u'https://twitter.com/BarackObama'
browser.get(url)
time.sleep(1)

body = browser.find_element_by_tag_name('body')

for i in range(100):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

tweets = browser.find_elements_by_class_name('tweet-text')
source = browser.page_source
soup = bs.BeautifulSoup(source,'lxml')

f= open("ObamaTwitter.txt","w+")
for m in tweets:
 print(m.text)
 f.write(m.text)
 f.write("\n")
 f.write("\n")

f.write("Tweeted by:"get_handle(soup))
f.close()


def get_handle(BSobject):
    for handle in BSobject.find_all('a', class_='ProfileHeaderCard-screennameLink u-linkComplex js-nav'):
        for at in handle.find_all('b', class_='u-linkComplex-target'):
            print(at.text)
    return(at.text)
