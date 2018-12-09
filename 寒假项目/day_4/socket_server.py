#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import socket,os,time
server=socket.socket()#创建 一个socket对象
server.bind(('localhost',9090))#绑定监听端口
server.listen()#监听
print('waitting...')
while True:
    conn,addr=server.accept()#等电话打过来
    #conn就是客户端连过来在服务端生成的一个实例
    print(addr)
    print('is comming ')
    while True:
        print("等待新指令：")
        data=conn.recv(1024)
        print('执行命令：',data)
        cmd_res=os.popen(data.decode(),'r').read()
        print('recv_size:',cmd_res)
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        time.sleep(0.5)#防止linux缓冲区黏住，让上一个缓冲区类容过期（粘包）
        conn.send(cmd_res.encode('utf-8'))
server.close()
