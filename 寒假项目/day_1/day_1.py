#!/usr/bin/env python
# Auther:Cray
# -*- coding:utf-8 -*-
'''f_bak=open ('dir.bak','r+',encoding='utf-8')
with open('dir','r+',encoding='utf-8') as f:

    for i in f.readlines():
        if '舌尖上的雨露' in i:
            i=i.replace('舌尖上的雨露','Crat')
        f_bak.write(i)
f_bak.close()
'''
with open('dir','r+',encoding='utf-8') as f\
        :
    print(f.read())