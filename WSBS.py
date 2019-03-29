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

















'''
source = urllib.request.urlopen('https://twitter.com/jimmyfallon?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor').read()
soup = bs.BeautifulSoup(source,'lxml')

def get_handle(BSobject):
    for handle in BSobject.find_all('a', class_='ProfileHeaderCard-screennameLink u-linkComplex js-nav'):
        for at in handle.find_all('b', class_='u-linkComplex-target'):
            print(at.text)
    return(at.text)

def date_of_tweet(BSobject):
    for span in BSobject.find_all('a', class_='tweet-timestamp js-permalink js-nav js-tooltip'):
        print(span.text)
        for m in span.find_all('span'):
            print(m.text)
    get_handle(BSobject)


'''
'''
for div in soup.find_all('div',class_='content'):
    for child1 in div.find_all('div',class_='js-tweet-text-container'):
        print(child1.text)
'''
'''
get_handle(soup)
date_of_tweet(soup)





'''

'''
source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')
table = soup.table
table = soup.find('table')
table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

dfs= pd.read_html('https://pythonprogramming.net/parsememcparseface/')
for df in dfs:
    print(df)
'''







"""
nav = soup.nav
for div in soup.find_all('div',class_='body'):
    print(div.text)

body = soup.body
for paragraph in body.find_all('p'):
    print(paragraph.text)

for url in nav.find_all('a'):
    print(url.get('href'))

print(nav)
print(soup.find_all('p'))
for paragraph in soup.find_all('p'):
    print(paragraph.text)

print(soup.get_text())

for url in soup.find_all('a'):
    print(url.get('href'))

"""
