#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import urllib2,chardet
import json
import jsonpath
url='https://www.lagou.com/lbs/getAllCitySearchLabels.json'
req=urllib2.Request(url)
response=urllib2.urlopen(req)
html=response.read()
jsonobj=json.loads(html)

city=jsonpath.jsonpath(jsonobj,'$..name')

with open('city.txt','w') as f:
    city2=json.dumps(city,ensure_ascii=False)
    f.write(city2.encode('utf-8'))