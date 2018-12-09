#!/usr/bin/env python
# __Author__:Cray
# -*- coding:utf-8 -*-
import os
import sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PATH)
user_right='ray'
password_right='lei123'
import conf
import json
import time
login_statu = False
def login(func):
    def inner(*args,**kwargs):
        global login_statu
        while login_statu==False:
            user=input("请输入账号：").strip()
            password=input("请输入密码：").strip()
            if user==user_right and password==password_right:
                print('登陆成功：')
                login_statu=True
                return func(*args,**kwargs)
            else:
                print('请重新输入\n')
        else:
            return func()
    return inner



'''{"all_money": 18000,
"name":"ray"
}'''
def czl():#查总量 返回字典
    with open('../conf/setting', 'r') as f_1:
        setting = json.loads(f_1.read())
    return setting
def change_money(setting,number):#使用或存钱
    with open('../conf/setting', 'w') as f_1_1:
        setting['all_money']+=number
        #print('剩余金额：',setting['all_money'])
        json.dump(setting,f_1_1)
    return setting
@login
def use_money(price):
    setting=czl()
    if setting['all_money']>=price:
        price=-price
        change_money(setting,price)
        print('你还剩：',setting['all_money'])
    else:
        print("钱不够，还剩：",setting['all_money'])

@login
def save_money(number):
    setting=czl()
    setting=change_money(setting,number)
    print(setting['all_money'])
@login
def you_all():
    setting=czl()
    print(setting['all_money'])
def  main(*args):#剩余钱，存钱，取钱
    #print('卡上剩余：',czl()['all_money'])
    set_number=input("你要进行的操作：1:存钱 2：取钱 3：查存款")
    if set_number.isdigit():
        set_number=int(set_number)
        if set_number==1:
            while True:
                number=input("你要存多少钱？请输入：")
                if number.isdigit():
                    number=int(number)
                    save_money(number)
                    break
                else:
                    print("输入错误，重新输入")
        elif set_number==2:
            price=input("请输入你要取的钱：")
            if price.isdigit():
                price=int(price)
                use_money(price)
        elif set_number==3:
            you_all()
        else:
            print("eee")
    else:
        print('有问题啊')

main()


