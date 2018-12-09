#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import re
def express(express):
    '''

    :param express:
    :return:
    '''
    express=express.replace('-+','-')
    express=express.replace('--','+')
    express=express.replace('+-','-')
    express=express.replace('*-','*')
    return express
def js(num):
    '''
    传入最里面括号里面的整个式子
    :param num:
    :return:
    '''
    while re.search('[0-9.]+[\+\-\*\/]',num):#判断是不是还有加减乘除。
        print('每次计算的过程',num)
        if re.search('[0-9.]+[\/\*][0-9.]+', num):
            num = express(num)
            res=re.search('[0-9.]+[\/\*][0-9.]+', num)
            loc_1, loc_2 = res.span()
            #print(type(num[loc_1:loc_2]))
            num = num.replace(num[loc_1:loc_2],cc(res.group()))

        elif re.search('[0-9.]+[\+\-][0-9.]+',num):
            num=express(num)
            res_2=re.search('[0-9.]+[\+\-][0-9.]+', num)
            print(res_2)
            loc_21, loc_22 = res_2.span()
            if res_2:
                num = num.replace(num[loc_21:loc_22], jj(res_2.group()))
        else:
            print('js have truble!!!')
            break;
    else:
        num = express(num)
        return num

def jj(num):
    '''return all laster number
    :num  a not have '()' numbers
    :return 计算结果
    '''
    if re.search('^[0-9.]\-',num):
        n1,n2=re.split('^[0-9.]\-',num)
        ret = float(n1) - float(n2)
        return str(ret)
    elif re.search('^[0-9.]\+',num) :
        n1,n2=re.split('^[0-9.]\+',num)
        ret = float(n1) + float(n2)
        return str(ret)
    else:print('加减有问题啊。。。')

def cc(num):
    if '*' in num:
        n1,n2=re.split('\*',num)
        ret = float(n1) * float(n2)
        return str(ret)
    elif '/' in num :
        n1,n2=re.split('\/',num)
        ret=float(n1)/float(n2)
        return str(ret)
    else:print('乘除有问题。。。')
def delkh(num):
    '''去括号
    :num 有括号的数据
    :return 没有括号数据 '''
    start=re.search('[()]',num)
    if start:
        num=num[1:len(num)-1]
        return num
    else:
        print(' 没括号了')
def main():
    exa='1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
    #exa='-1388337.0476190478+12.0/10.0'
    while True:
        res=re.search('(\([\-\+\*\/.0-9]+\))',exa)
        if res:
            k=res.group()
            loc=res.span()
            num_1=delkh(k)
            print('计算的一个式子',num_1)
            rep=js(num_1)
            print('这个式子的结果：',rep)
            exa=exa.replace(exa[loc[0]:loc[1]],rep)
            print(exa)
            exa = express(exa)

        else:
            print('结束了，答案是：',js(exa))
            break
main()