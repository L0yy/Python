#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4" )
driver = webdriver.PhantomJS(executable_path=r'C:\Users\lm163\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe',desired_capabilities=dcap)
print 'connect....'

driver.get('http://new.shunderen.com/member.php?mod=register')


time.sleep(2)
driver.save_screenshot('1.png')
a=driver.find_element_by_xpath('//*[@id="vseccode_cSk2jah0"]/img')
print a
