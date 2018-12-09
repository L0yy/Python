#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-

import socket
client=socket.socket()
client.connect(('localhost',9090))

while True:
    res=input('请输入你命令>>:').strip().encode('utf-8')
    '''python3 中的传输是bytes流，传输前要encode，接收后的数据要decode 才能正确显示中文
    还要注意一个中文 str 类型是占1个字节  bytes类型是占3个字节'''
    client.send(res)
    res_data_size=0
    res_data=b''
    data_size = client.recv(1024)
    while res_data_size!=int(data_size.decode()):
        data=client.recv(1024)
        res_data+=data
        res_data_size=len(res_data)
        print("data_size:",data_size.decode())
        print('res_data_size',res_data_size)

    else:
        print('接收完成，接受总大小：',len(res_data))
        print('recv:',res_data.decode())

client.close()