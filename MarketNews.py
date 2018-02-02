#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:26:33 2018

@author: shockwave
"""


import requests
from bs4 import BeautifulSoup
url = "http://finance.google.com/finance/market_news?ei=IbdpWqiTEYWsugSGh4-4Ag"
doc = requests.get(url)
soup= BeautifulSoup(doc.content, "html.parser")
k =[]
m=[]
k= soup.findAll("div",class_="g-section news sfe-break-bottom-16")
#print(len(k))
#for _ in k[:]:
#    m = soup.find("div",style="width:100%;").get_text()
#    print(m);print("\n")
#    
m= soup.findAll("div",style="width:100%;")
l= soup.findAll("div",class_="byline")
print("\n")
print("Daily News from Google Finance!!\n----------------------------------------------------")
u=soup.findAll("span",class_="name")
for i in range(len(k)):
    print(u[i].text)
    print(l[i].text);
    print(m[i].text);print("\n")
    print("---------------------------------------------------------")
    
    