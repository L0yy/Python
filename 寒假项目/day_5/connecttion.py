#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
from pymysql import *
try:
    #charset要写utf8 不能些utf-8
    coon= connect(host='192.168.16.131',user='root',password='123456',port=3306,database='test',charset='utf8')#charset要写utf8 不能些utf-8
    curs=coon.cursor()
    sql='select * from ouer; '.encode()
    result=curs.execute(sql)#提交命令
    ks=curs.fetchall()#查看返回的结果集
    print(result,ks)
    curs.close()
    coon.close()
except Exception as e:
    print(e)