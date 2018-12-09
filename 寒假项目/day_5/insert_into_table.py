#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import os,sys
path=os.path.dirname(__file__)
sys.path.append(path)
from Mysqlhelper import *
try:
    coon=MysqlHelper(host='192.168.16.131',user='root',passwd='123456',port=3306,db='test')
    sql="select * from %s"
    sname=input("请输入你查询的表名：").strip()
    sql=sql.replace('%s',sname)
    list_1=coon.get_all(sql)
    print(list_1)
    coon.close()
except Exception as e:
    print(e)
