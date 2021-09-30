# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 20:00:13 2021

@author: USER
"""
import requests
import db
from bs4 import BeautifulSoup
url = 'https://tw.buy.yahoo.com/category/40057185'
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}
data = requests.get(url,headers=header)
data.encoding = 'UTF-8'
data = data.text
soup = BeautifulSoup(data,'html.parser')
goods = soup.find_all('li',class_='BaseGridItem__grid___2wuJ7 BaseGridItem__multipleImage___37M7b')
for i in goods:
    link = i.a.get('href')
    name = i.img.get('alt')
    images = i.img.get('srcset').split()[0]
    title = i.find('span',class_='BaseGridItem__title___2HWui').text
    price = i.find('em').text
    price = price.replace('$','').replace(',','')
    

    sql = "insert into products(Shop,Name,Price,Photo_Url,link,Product_type) values('Yahoo','{}','{}','{}','{}',1)".format(name,price,images,link)
    db.order.execute(sql) #執行
    db.conn.commit() #提交
