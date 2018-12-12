# -*- coding=utf-8 -*-
from multiprocessing import Process
import gevent
from gevent import monkey;monkey.patch_all()
import urllib
from lxml import etree
import os,time
import http.cookiejar
save_path = '/home/c/bed/'#writter you want save path
def savejpg(url):
    head = {"Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": " zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7 ",
            "Cache-Control": " max-age=0 ",
            "Connection": " keep-alive ",
            "Host": " okl.scene7.com ",
            "If-Modified-Since": " Thu, 24 Aug 2017 21:15:59 GMT ",
            "If-None-Match": "364807b80f9e39e5083acc91b692f9af",
            "Upgrade-Insecure-Requests": " 1 ",
            "User-Agent": " Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36 ", }

    path_name = str(url).split('.')[0].split('/')[-1]
    now_path = save_path + path_name

    print('this is now cwd', os.getcwd())
    baseurl = 'https://www.onekingslane.com'
    new_url = baseurl + str(url)
    print("new_base:",new_url)
    res = net_urllib(new_url)
    res_x = etree.HTML(res)
    img_urls = res_x.xpath("//div[@id='ml-alternate-images-source-xs']//img/@src")  # 获取到具体图片urls
    img_urls = list(set(img_urls))  # 去重
    for i in img_urls:
        if not os.path.exists(now_path):
            os.mkdir(now_path)  # 创建要保存到的目录
        name = i.split('/')[-1].split('$')[0] + 'jpg'
        print ('name',name)
        a = urllib.request.Request(i, data=None, headers=head)
        img_data = urllib.request.urlopen(a).read()
        os.chdir(now_path)
        with open(name, 'wb') as fd:
            #print(now_path)
            fd.write(img_data)
            print ("[*]write over", os.getcwd())
def net_urllib(in_url):
    ''' head = {
     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
     "accept-encoding": "gzip, deflate, br",
     "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
     "cookie": "customer=none; basket=none; optimizelyEndUserId=oeu1537881881002r0.7119070451849805; _ga=GA1.2.1102514736.1537881881; _gid=GA1.2.1266036178.1537881881; JSESSIONID=6C499D3433F73D3BFE755BADF7854907.b2c-onekingslane-prdv162-app001; e66=1; v40=ourPicksAscend; AMCVS_%20261F337B54E73B180A4C98A1%40AdobeOrg=1; AMCV_%20261F337B54E73B180A4C98A1%40AdobeOrg=-1891778711%7CMCIDTS%7C17800%7CvVersion%7C2.4.0%7CMCMID%7C48960352836016860504917301348217204080%7CMCOPTOUT-1537966335s%7CNONE; c10=furniture%20%3E%20living%20room%20%3E%20sofas%20and%20settees; c25=https%3A%2F%2Fwww.onekingslane.com%2Fc%2Ffurniture%2Fliving%2Broom.do; c38=product%20listing; s_cc=true; _br_uid_2=uid%3D9897515959825%3Av%3D11.8%3Ats%3D1537959150770%3Ahc%3D1; cto_lwid=cb99f698-3807-43d5-bb25-2c7ff91c65a5; _gat=1; utag_main=v_id:016610e74599008ba22c27d36b0803068007106000bd0$_ss:0$_st:1537961801320$vapi_domain:onekingslane.com$ses_id:1537959421680%3Bexp-session",
     "upgrade-insecure-requests": 1,
     "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36", }
 cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
 handler = urllib.request.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
 opener = urllib.request.build_opener(handler)  # 通过handler来构建opener
 request = urllib.request.Request(url=in_url, data=None, headers=head)
 res = opener.open(request).read()  # # 此处的open方法同urllib2的urlopen方法，也可以传入request
 return res'''
    head = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "customer=none; basket=none; optimizelyEndUserId=oeu1537881881002r0.7119070451849805; _ga=GA1.2.1102514736.1537881881; _gid=GA1.2.1266036178.1537881881; JSESSIONID=6C499D3433F73D3BFE755BADF7854907.b2c-onekingslane-prdv162-app001; e66=1; v40=ourPicksAscend; AMCVS_%20261F337B54E73B180A4C98A1%40AdobeOrg=1; AMCV_%20261F337B54E73B180A4C98A1%40AdobeOrg=-1891778711%7CMCIDTS%7C17800%7CvVersion%7C2.4.0%7CMCMID%7C48960352836016860504917301348217204080%7CMCOPTOUT-1537966335s%7CNONE; c10=furniture%20%3E%20living%20room%20%3E%20sofas%20and%20settees; c25=https%3A%2F%2Fwww.onekingslane.com%2Fc%2Ffurniture%2Fliving%2Broom.do; c38=product%20listing; s_cc=true; _br_uid_2=uid%3D9897515959825%3Av%3D11.8%3Ats%3D1537959150770%3Ahc%3D1; cto_lwid=cb99f698-3807-43d5-bb25-2c7ff91c65a5; _gat=1; utag_main=v_id:016610e74599008ba22c27d36b0803068007106000bd0$_ss:0$_st:1537961801320$vapi_domain:onekingslane.com$ses_id:1537959421680%3Bexp-session",
        "upgrade-insecure-requests": 1,
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36", }

    request = urllib.request.Request(url=in_url,data=None,headers=head)
    res = urllib.request.urlopen(request).read().decode('utf-8')
    #print("xiazia zhegedizhi ",in_url)
    return res

def process_start(op_url):
    print("[*]begin ", os.getpid())
    tasks = []
    res = net_urllib(op_url)
    res_x = etree.HTML(res)
    url_list = res_x.xpath("//div[@class='ml-thumb-image']/a/@href")  # 每个商品页面
    #print("[/]success get ever page  all商品!!!!")
    for url in url_list:
        print ("[/] 开始协程 down jpg:", url)
        tasks.append(gevent.spawn(savejpg, url))
    gevent.joinall(tasks)  # 使用协程来执行
    print("[*]end ", os.getpid())

def task_start(filepath):
    with open(filepath, 'r') as reader:  # 从给定的文件中读取url
        url = reader.readline().strip()
        while url != '':
            # print('[*]begin Process!!!!',url)
            p = Process(target=process_start, args=(url,))  # 
            # print('[/]err')
            p.start()
            url = reader.readline().strip()
            time.sleep(10)

if __name__ == '__main__':
    task_start('./urls.txt')  # 读取指定文件
