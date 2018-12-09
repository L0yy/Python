#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import os,sys
import hashlib

path=os.path.dirname(__file__)
sys.path.append(path)
from Mysqlhelper import *

stu_id=input('学号>>：').strip()
sql = 'select * from student where student_id = $s1 '
sql = sql.replace('$s1', stu_id)

try:
    coon = MysqlHelper(host='192.168.16.131', user='root', passwd='123456', port=3306, db='NSU')
    result = coon.get_all(sql)
    right_passwd = result[0][1]
    print(right_passwd)
except Exception as e:
    print(e)
stu_pwd=''
while True:
    if stu_pwd != right_passwd:
        stu_pwd=input("密码>>:").strip()
        stu_pwd=hashlib.md5(stu_pwd.encode()).hexdigest()
        print(stu_pwd)
        print('密码错误：重新输入')
    elif stu_pwd == right_passwd:
        print(result)
        break