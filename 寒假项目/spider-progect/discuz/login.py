#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import  time


class dsc():
    @staticmethod
    def login():
        print 'setting PhantomJS...'
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4" )
        driver = webdriver.PhantomJS(executable_path=r'C:\Users\lm163\Downloads\phantomjs-2.1.1-windows\bin\phantomjs.exe',desired_capabilities=dcap)
        print 'connect....'

        driver.get('http://new.shunderen.com/forum.php')
        driver.save_screenshot('login_1.png')
        driver.find_element_by_name('username').send_keys("cray")
        driver.find_element_by_name('password').send_keys("Ll123123")
        driver.find_element_by_xpath("//button[@class='pn vm']").click()
        print "loginning..."

        time.sleep(3)#waitting 3 second
        driver.save_screenshot('login_2.png')


        print driver.find_element_by_xpath("//span[contains(@id,'vseccode')]").screenshot('logon_4.png')
        print 'exit..'

        driver.quit()
    def work_yzm(self):
        pass



if __name__ == '__main__':
    test=dsc()
    dsc.login()

