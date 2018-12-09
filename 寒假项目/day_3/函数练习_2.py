#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
class pretect(object):#
    '''
    面向对象编程，如果是函数式编程的话就没有class定义的类
    '''
    def __init__(self,name,age,sex,thing):
        self.name=name
        self.age=age
        self.sex=sex
        self.thing=thing
    def kancai(self):
        print('%s,%s岁,%s,喜欢砍柴' %(self.name,self.age, self.sex))
    def kaiche(self):
        print('%s,%s岁,%s,喜欢开车' %(self.name,self.age, self.sex))
    def sj(self):
        print('%s,%s岁,%s,喜欢睡觉' %(self.name,self.age, self.sex))
xm=pretect('rat',11,'男','hahah ')
xm.kaiche()
xm.kancai()
print(xm.name)