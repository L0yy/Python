#-------------------------------------------------------------------------------
# Author:      Crayon
# Created:     29/11/2018
# Copyright:   (c) Crayon 2018
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: UTF-8 -*
#coding=utf-8
import urllib
import urllib2
import json
from lxml import etree
locat = 1    #要选课的位置
name = "453"   #课名
xh = 163101    #你的学号
bj = 64        #你的班级
#Cookei值一定也要记得修改

def req(url,data=None):
    #这个cookie就是你们账号登录后的cookie
    cookie = "analytics=a1e9736d5bda5dc6; PHPSESSID=85511735afdea0617f330c23609af66e; YB_SSID=9af171ca4b0a04f7b2941a34c30e34b8; yiban_user_token=7d93e3616df304e9df2cd763fb157f30; _YB_OPEN_V2_0=mg0lM_0_2Fphp01m; timezone=-8; laravel_session=eyJpdiI6IjdKalwvTVErZG9aUXlDcUV6MklFdmZBPT0iLCJ2YWx1ZSI6IklyeSt3NTRCN0VXVzZPMklQQVU2bzhcL3JTZlBycUxqUUNZN2V4N1Myb1BqMDV6RzFWXC9JZWo2elVmb3I1TlAzODUrYURVVkVaTnR5WmRIQkp5NFE2Nmc9PSIsIm1hYyI6IjY3YjU2N2NmZDQ5MjViNWZjMGU1MDM3ZWE1OWRjODI2OWNmZGNjZmI4ZWUwNmMxN2NmZTczNzgzZDNkZjZmYzgifQ%3D%3D"
    header={
    "Cookie": cookie,
    "User-Agent":" Mozilla/5.0 (X11; Linux i686; rv:60.0) Gecko/20100101 Firefox/60.0",

}
    if data!=None:
        #print data
        data = urllib.urlencode(data)
        request = urllib2.Request(url, data=data, headers=header)
        response = urllib2.urlopen(request)
        return response.read()
    else:
        request = urllib2.Request(url,headers=header)
        response = urllib2.urlopen(request)
        return response.read()

def sea_add(name,i):
    #根据名字搜索，并添加到自己的应用中，返回url地址最后一个参数
    url = "http://app.yiban.cn/apps/search"
    data = {
    "search_key": name
    }
    response = req(url,data)
    html = etree.HTML(response)
    #print html
    url_code = html.xpath("//div[@class='appName']//button/@appid")
    App_id = html.xpath("//div[@class='appName']/a/@href")

    #print url_code    #这个也是提交页的参数
    data2={
    "app_id":url_code[i-1],
    "act" : "add",
    "position":5}
    url2 = "http://app.yiban.cn/ajax/visitapp"
    ret = req(url2,data2)
    if ret[7:10]=='cha' :
        print "[/]添加课程成功"
    response = req(url,data)
    html = etree.HTML(response)
    App_id = html.xpath("//div[@class='appName']/a/@href")
    print "[—]获取主页地址成功"
    return App_id


def get_code(urll):
    #返回选课所用code值
    response = req(urll)
    html = etree.HTML(response)
    js_data = html.xpath('/html/head/script[1]/text()')
    ss = str(js_data[0].encode('utf-8')).replace(' ','').split(',')[51].split(':')[-1]
    print "[\]code查找成功"
    return ss

def get_id(App_id,code):
    #选课页面的url
    #cookie都是个人的
    #code是选课页面上获取到的值
    url = 'https://q.yiban.cn/signup/getSignupAjax'
    data = {
        "App_id": eval(App_id),
        "code": eval(code),
    }
    #print data
    respose = req(url,data)
    rt = respose.decode('unicode_escape').encode('utf-8').split(":")[4].split(',')[0]
    print "[-]id查找成功"
    return eval(rt)

def tijiao(App_id,id,xh,bj):
    url = "https://q.yiban.cn/signup/insertBoxAjax"
    data = {
    "App_id":eval(App_id) ,
    "id":id,
    "flag":" 1" ,
    "answers[]":str(xh) ,
    "answers[]":str(bj),
    }
    response_texte = req(url,data).decode('unicode_escape')
    return response_texte



def main():
    url = sea_add(name,locat)[0]
    #url = 'https://q.yiban.cn/app/index/appid/259170'
    App_id = url.split('/')[-1]
    code = get_code(url)#
    id = get_id(App_id,code)
    print id
    print tijiao(App_id,id,xh,bj).split(':')[-1][:-1]


if __name__ == '__main__':
    main()