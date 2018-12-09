#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import configparser
conf=configparser.ConfigParser()
conf.read('configparser_file.txt',encoding='utf-8')

ret=conf.sections()#返回所有节点
print(ret)

ret=conf.items('person_1')#返回所有键值对
print(ret[0])

v=conf.get('person_1','name')#获取指定节点下指定key的值
print(v)

f=conf.has_section('person_3')#检测这个节点是否存在，不存在返回False
print(f)

conf.set('person_1','class','55')#设置键值对
conf.write(open('configparser_file.txt','w'))
