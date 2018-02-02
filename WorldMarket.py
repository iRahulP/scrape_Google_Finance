#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 17:26:57 2018

@author: shockwave
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "http://finance.google.com/finance?ei=msJxWsjWBdKRuQTjiojIAg"
doc = requests.get(url)
soup= BeautifulSoup(doc.content,"html.parser")

k=l=m=""
k = soup.find("td",class_="symbol").text
v=k.encode('ascii')

l=[]
l=list(v.split("\n"))
l.pop()
st = ""
name=[]
for i in range(len(l)):
    if i%3==0:
        name.append(l[i])

price=[]

for i in range(len(l)):
    if i%3==1:
        price.append(l[i])

change=[]

for i in range(len(l)):
    if i%3==2:
        change.append(l[i])

        
data = {'Name': name,'Price': price,'Change': change}
f=pd.DataFrame(data, columns=['Name','Price','Change'] )
print "*****************  WORLD MARKETS INFO  *********************"
print f
