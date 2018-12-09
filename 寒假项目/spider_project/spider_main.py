#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import urllib2,re
class Spider():
    def loadpage(self):
        url="http://www.neihan8.com/article/list_5_1.html"
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
        req=urllib2.Request(url,headers=header)
        response=urllib2.urlopen(req)
        html=response.read().decode('gbk')
        return html
    def print_onepage(self,html,page):
        pass

    def re_html(self,html):
        pattern=re.compile(r'<div class="f18 mb20">(.*?)</div>',re.S)
        all_list=pattern.findall(html)
        pattern = re.compile(r'<a href="/article/[0-9]*.html">(.*?)</a>', re.S)
        title_all=pattern.findall(html)
        all_list2=''
        all_list3=''
        title_all2=''
        for i,j in (all_list,title_all):
            title_all2=title_all2+(j.encode("utf-8"))
            all_list2=all_list2+(i.encode("utf-8"))
            all_list3=title_all2+'/n'+all_list2
        return all_list3


spider=Spider()
html=spider.loadpage()
all_list=spider.re_html(html)
print all_list

