# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 21:10:25 2021

@author: USER
"""

import db
import requests
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


    sql = "select price from products where link='{}'".format(link)
    db.order.execute(sql)
    db.conn.commit()
    #result = db.order.fetchall() #fetchall()抓取所有的資料
    if db.order.rowcount == 0:
        sql = "insert into product(shop,name,price,photo_url,link,product_type) values('Yahoo','{}','{}','{}','{}',1)".format(name,price,images,link)
        db.order.execute(sql)
        db.conn.commit()
    else:
        result = db.order.fetchone()
        if result[0] != int(price):
            print('價格不同')
db.conn.close()