# -*- coding: utf-8 -*-
import bs4 as bs
import urllib.request
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

pagenumber = [str(i)for i in range(1)]
print(pagenumber)

def get_club_name(soup,list):
    for section in soup.find_all('section', class_='main-content-area'):
        for div in section.find_all('div', class_='view-content'):
            for H in div.find_all('h2', class_= 'field-content'):
                print(H.text)
                list.append(H.text)

def get_club_description(soup,list):
    for section in soup.find_all('section', class_='main-content-area'):
        for div in section.find_all('div', class_='field-content'):
            for H in div.find_all('p'):
                list.append(H.text)

def get_club_catogories(soup,list):
    m=[]
    n=0
    for section in soup.find_all('section', class_='main-content-area'):
        for fib in section.find_all('div', class_='views-field views-field-field-clubs-categories club-category'):
            for div in fib.find_all('div', class_='item-list'):
                for H in div.find_all('li'):
                    m.append(H.text)
                    print(m)
                    print(list)
                    list.append(m)
                    m.clear()






clubname=[]
clubdescription=[]
clubcatagories=[]


for i in pagenumber:
    source = urllib.request.urlopen('https://feds.ca/clubs/listing?page='+ i ).read()
    soup = bs.BeautifulSoup(source,'lxml')
    #get_club_name(soup,clubname)
    #get_club_description(soup,clubdescription)
    get_club_catogories(soup,clubcatagories)

data3 = zip(clubcatagories)
df3 = pd.DataFrame(data3, columns=['Club catagories'])
df3.to_csv('clubcatagories.csv')


'''
data1 = zip(clubname)
df = pd.DataFrame(data1, columns=["Clubname"])
df.to_csv('Clubname.csv')

data2 = zip(clubdescription)
df2 = pd.DataFrame(data2, columns=["Club Desctiption"])
df2.to_csv('ClubDesctiption.csv')

clubname.append(get_club_name(soup))
def get_club_description(soup):
    for section in soup.find_all('section', class_='main-content-area'):
        for div in section.find_all('div', class_='field-content'):
            for H in div.find_all('p'):
                return(H.text)
print(clubname)
data1 = zip(clubname)
data2 = zip(clubdescription)
df = pd.DataFrame(data1, columns=["Clubname"])
df2 = pd.DataFrame(data2, columns=["Club Desctiption"])
df.to_csv('Clubname.csv')
df2.to_csv('ClubDesctiption.csv')
'''
