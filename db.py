# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql
conn = pymysql.connect(host = 'localhost',
                       user = 'root',
                       passwd = '123456789',
                       db = 'lccnet')
order = conn.cursor()