#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
from selenium import webdriver
# import os,sys
# print sys.path


driver=webdriver.PhantomJS(executable_path=r'C:\Users\lm163\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe')
driver.get('http://www.baidu.com/')
data=driver.page_source.encode('utf-8')
driver.save_screenshot('www.sohu.png')
with open('baidu.txt','w') as f:
    f.write(data)
driver.quit()