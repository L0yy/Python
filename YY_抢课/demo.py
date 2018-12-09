# -*- coding: UTF-8 -*
import urllib
import urllib2
import json
from lxml import etree
locat = 1    #要选课的位置   这个暂时就是这样
name = "天府论坛第464期"   #课名   这个就写你要抢的课
xh = 163101    #你的学号
bj = 64        #你的班级
#Cookei值一定也要记得修改

def req(url,data=None):
    #这个cookie就是你们账号登录后的cookie
    cookie = "analytics=a1e9736d5bda5dc6; PHPSESSID=b4f7e22466c971db80d184f0410d7413; YB_SSID=94c25ff2b8d361829948702dda480f6c; timezone=-8; _YB_OPEN_V2_0=0-B000Kq61qnGl2u; yiban_user_token=e9a6d2203b4119043d57ca35e5fbce24; laravel_session=eyJpdiI6Ik5iSHAzbnN4bXBXVjAyYzBZMTJKUUE9PSIsInZhbHVlIjoiTThQOE9FWjhGZmRMZWZOTXNTQ1FVeWZLMW9qK3pFRlc3aEFUWTdmVnlzQTdjdlFnUmx4c05LTGtOWUFMOW4xNFNUM1o2UllESkErUEJnUVRKZTJmRmc9PSIsIm1hYyI6ImZiNGU3M2NhMjg5OTg0NDdhZWExMGQ4YmMyYzRlNzIxZTgzNTVkMzRmYjUwMzBiMjYwZTAwODM3MDY2NDIwOGYifQ%3D%3D"
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

#def sea_add(name,i):
def sea_add(name):
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
    #"app_id":url_code[i-1],
    "app_id":url_code[0],
    "act" : "add",
    "position":5}
    url2 = "http://app.yiban.cn/ajax/visitapp"
    ret = req(url2,data2)
    if ret[7:10]=='cha' :
        print ("[*]kc add success!!!.")
    response = req(url,data)
    html = etree.HTML(response)
    App_id = html.xpath("//div[@class='appName']/a/@href")
    print ("[*]main add success!!!")
    return App_id


def get_code(urll):
    #返回选课所用code值
    response = req(urll)
    html = etree.HTML(response)
    js_data = html.xpath('/html/head/script[1]/text()')
    ss = str(js_data[0].encode('utf-8')).replace(' ','').split(',')[51].split(':')[-1]
    print ("[*]code find success!!!")
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
    print ("[*]id find success!!!")
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
    #url = sea_add(name,locat)[0]
    url = sea_add(name)[0]
    print url
    #url = 'https://q.yiban.cn/app/index/appid/259170'
    App_id = url.split('/')[-1]
    code = get_code(url)#
    id = get_id(App_id,code)
    #print id
    ress = tijiao(App_id,id,xh,bj).split(':')[-1].split('\"')[1]
    print ress


if __name__ == '__main__':
    main()