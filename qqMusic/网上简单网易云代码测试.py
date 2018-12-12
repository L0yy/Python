#coding=utf-8
from Tkinter import *
import  tkMessageBox
import urllib
import json
import mp3play
import time
import threading
from pinyin import PinYin
import os
import stat
test = PinYin()
test.load_word()
stop=0
def music():
    
    if not entry.get():
        tkMessageBox.showinfo("温馨提示","搜索内容不能为空")
        return
    name = test.hanzi2pinyin_split(entry.get())
    html=urllib.urlopen("http://s.music.163.com/search/get/?type=1&s=%s&limit=9"%name).read()
    js=json.loads(html)
    n = 0
    global x
    x = []
    for i in js['result']['songs']:
        listbox.insert(n,'%s(%s)'%(i['name'],i['artists'][0]['name']))
        n+=1
        x.append(i['audio'])
count = 0
#isplaying = None
def play():
    global count
    count += 1
    number
    index=listbox.curselection()
    var1.set(u"正在加载"+listbox.get(index,last=None))
    urllib.urlretrieve(x[index[0]],'tmp%s.mp3'%str(count))
    var1.set(u"正在播放"+listbox.get(index,last=None))
    mp3=mp3play.load("tmp%s.mp3"%str(count))
    mp3.play()
    time.sleep(mp3.seconds())
 
import inspect
import ctypes
 
def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")
 
def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)
threads=list()
t=None
def excute(event):
    global  t
    for i in threads:
        stop_thread(i)
    t = threading.Thread(target=play)
    t.setDaemon(True)
    t.start()
    threads.append(t)
root = Tk()#创建一个窗口
root.title("云音乐")
root.geometry("500x300+500+200")
entry=Entry(root)#创建输入框（单行）,置父
entry.pack()
btn=Button(root,text="搜 索",command=music)
btn.pack()#布局方式必须用同一种
var=StringVar()
listbox=Listbox(root,width=50,listvariable=var)
listbox.bind('<Double-Button-1>',excute)
listbox.pack()
var1=StringVar()
label=Label(root,text="云音乐播放器",fg="purple",textvariable=var1)
var1.set("云音乐播放器")
label.pack()
root.mainloop()#显示窗口
