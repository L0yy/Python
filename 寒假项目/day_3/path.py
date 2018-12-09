#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
# import hashlib
# print(help(hashlib))
# a=hashlib.md5()
# b=hashlib.md5()
# a.update(b"b")
# a.update(b"a")
# b.update(b"ba")
# print(b.hexdigest())
# print(a.hexdigest())
import os,sys
path1=os.path.abspath(__file__)#获取工作目录
print(sys.path)
print(sys.path.append(path1))