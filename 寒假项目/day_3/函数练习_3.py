#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
# class Role(object): #定义一个类， class是定义类的语法，Role是类名，(object)是新式类的写法，必须这样写，以后再讲为什么
#     def __init__(self,name,role,weapon,life_value=100,money=15000): #初始化函数，在生成一个角色时要初始化的一些属性就填写在这里
#         self.name = name #__init__中的第一个参数self,和这里的self都 是什么意思？ 看下面解释
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money


class SchoolMember(object):
    members = 0  # 初始学校人数为0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        pass

    def enroll(self):
        '''注册'''
        SchoolMember.members += 1
        print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " % (
        self.name, SchoolMember.members))

    def __del__(self):
        '''析构方法
        调用完了后，执行析构函数。
        '''
        print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)


class Teacher(SchoolMember):
    def __init__(self, name, age, course, salary):
        super(Teacher, self).__init__(name, age)
        self.course = course
        self.salary = salary
        self.enroll()

    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, 'Oldboy', self.course)
        print(msg)


class Student(SchoolMember):
    def __init__(self, name, age, grade, sid):
        super(Student, self).__init__(name, age)
        self.grade = grade
        self.sid = sid
        self.enroll()

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], I'm studying [%s] in [%s]!''' % (self.name, self.grade, 'Oldboy')
        print(msg)


if __name__ == '__main__':
    t1 = Teacher("Alex", 22, 'Python', 20000)
    t2 = Teacher("TengLan", 29, 'Linux', 3000)

    s1 = Student("Qinghua", 24, "Python S12", 1483)
    s2 = Student("SanJiang", 26, "Python S12", 1484)

    t1.teaching()
    t2.teaching()
    t1.tell()