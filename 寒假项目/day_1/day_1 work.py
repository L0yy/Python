#!/usr/bin/env python
#_*_coding:utf-8*_
# Auther:Cray
#-*-coding:utf-8 -*-
f=open("work_init",'r+')
sc=int(input("查询：1\n新建：2\n删除：3\n"))
if (sc==1):
    cat=str(input("查询的语句："))
    for i in f:
        if cat in i:
            print(i)
f.close()