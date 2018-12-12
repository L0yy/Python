
# -*- encoding:utf-8 *-*

from urllib import request,parse
import json

def main():
    sea = input("你要搜索的歌曲：").strip()

    url1 = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=62141820259095437&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}&g_tk=5381&jsonpCallback=MusicJsonCallback803587099861895&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0".format(parse.quote(sea))
    response1 = get_res(url1)

    js = get_json(response1)

    mid  = []
    name =[] 
    singer = []
    for loc in range(20):
        try:
            mid.append(js['data']['song']['list'][loc]['mid'])#mid值
            name.append(js['data']['song']['list'][loc]['name'])
            singer.append(js['data']['song']['list'][loc]['singer'][0]['name'])
        except:
            mid.append('')
            name.append('')
            singer.append('')
        pr ="版本号:{:>2}======>{:<10}  演唱:  {}".format(loc+1,name[loc],singer[loc])
        print(pr)

    loc1 = input('你要听的版本(默认第一首)：').strip()
    loc1 = (0 if loc1 =='' else int(loc1)-1)

    url2 = '''https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey07513324702543245&g_tk=5381&jsonpCallback=getplaysongvkey07513324702543245&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"729527810","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"729527810","songmid":["'''+mid[loc1]+'''"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":20,"cv":0}}'''
    #print (url2)
    response2 = get_res(url2)

    js2 = get_json(response2)

    ip = js2['req']['data']['freeflowsip'][0]#获取歌曲地址域名部分
    uu = js2['req_0']['data']['midurlinfo'][0]['purl']#获取后面具体的链接
    url3 = ip+uu
    print(url3)

def get_json(response):
    flag = 0
    for s in response:
        if s =='(':
            flag += 1
            break
        flag += 1
    js = json.loads(response[flag:-1])
    return js

def get_res(url):
    header = {
        "accept":" text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-language":" zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control":" max-age=0",
        "cookie": "yq_index=0; yq_playschange=0; yq_playdata=; player_exist=1; yqq_stat=0; pgv_info=ssid=s6591267740; pgv_pvid=5882820530; ts_uid=9225584320; pgv_pvi=1484052480; pgv_si=s2212878336; qqmusic_fromtag=66; yplayer_open=0",
        "upgrade-insecure-requests": 1,
        "user-agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",}
    req = request.Request(url,headers=header)
    response = request.urlopen(req).read()
    response = response.decode('utf-8')
    return response

if __name__ == '__main__':
    main()
    
# def get_cookie():
#     url_test1 = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=62141820259095437&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=love&g_tk=5381&jsonpCallback=MusicJsonCallback803587099861895&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"
#     url_test = "https://www.baidu.com"
#     # 创建cookiejar实例
#     cookie = cookiejar.CookieJar()
#     # 创建管理器
#     cookie_handler = request.HTTPCookieProcessor(cookie)
#     http_handler = request.HTTPHandler()
#     https_handler = request.HTTPSHandler()
#     # 创建请求求管理器
#     opener = request.build_opener(cookie_handler, http_handler, https_handler)
    
#     req = request.Request(url_test)
#     response = opener.open(req)
#     print(response.reason)
#     print(cookie)  

# def ss():
#     mid = "***&&&****"
#     url = '''https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey07513324702543245&g_tk=5381&jsonpCallback=getplaysongvkey07513324702543245&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"729527810","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"729527810","songmid":[{"'''+mid+'''"}],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":20,"cv":0}}'''
#     #url = '''https://u.y.qq.com/cgi-bin/musicu.fcg?callback=getplaysongvkey07513324702543245&g_tk=5381&jsonpCallback=getplaysongvkey07513324702543245&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data={"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"729527810","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"729527810","songmid":["001cdurD2fY83O"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":20,"cv":0}}'''
#     #res = request.urlopen(url).read().decode()
#     print(url)






