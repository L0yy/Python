#coding=utf-8
#Version:python3.5.2
#Tools:Pycharm
#Date:2017-07-12
__author__ = "Colby"
'''
教程有瑕疵的地方请各位亲们万分理解，不胜感激
店主跟你们一起在学习哦，一定好好完成老师的作业！
好好利用资源，实现你们的人生价值。
'''
import re,os,sys
'''
计算这表达式的值：1 - 2 * ((60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2)))
'''
def format_mark(express):
    '''
    表达式替换过程中可能出现一些组合符号，
    机器无法辨别，此函数负责处理这些组合符号
    :param express:
    :return:
    '''
    express = express.replace('+-', '-')
    express = express.replace('-+', '-')
    express = express.replace('++', '+')
    express = express.replace('--', '+')
    express = express.replace('*+', '*')
    express = express.replace('+*', '*')
    express = express.replace('+/', '/')
    express = express.replace('/+', '/')
    return express
def com_jiajian(express):
    '''
    :param express:
    :return:
    '''
    expr = express
    sub_expr = re.search(r"\-?\d+\.?\d*[\+\-]\d+\.?\d*", expr)
    if not sub_expr:
        return expr
    else:
        sub_expr2 = sub_expr.group()
        # print('sub_expr1',sub_expr1,'19行结果express:',div_express)
        if len(sub_expr2.split('+')) > 1:
            n1, n2 = sub_expr2.split('+')
            result = float(n1)+float(n2)
        else:
            n1, n2 = sub_expr2.split('-')
            result = float(n1) - float(n2)
        re_sub_expr = re.sub(r"\-?\d+\.?\d*[\+\-]\d+\.?\d*", str(result), expr, count=1)
        # 反复调用除法
        print('加减运算：',re_sub_expr)
        bb = com_jiajian(str(re_sub_expr))
        return bb
def com_chengchu(expr_div):
    '''
    :param expr_div:
    :return:
    '''
    expr=expr_div
    sub_expr = re.search(r"\d+\.?\d*[\/\*]\-?\d+\.?\d*",expr)
    if not sub_expr:
        return expr
    else:
        sub_expr2 = sub_expr.group()
        if len(sub_expr2.split('/')) > 1:
            n1, n2 = sub_expr2.split('/')
            result = float(n1)/float(n2)
        if len(sub_expr2.split('*')) > 1:
            n1, n2 = sub_expr2.split('*')
            result = float(n1)*float(n2)
        else:
            #只计算乘除，加减直接pass，放入加减函数执行
            pass
        re_sub_expr=re.sub(r"\d+\.?\d*[\/\*]\-?\d+\.?\d*",str(result),expr,count=1)
        #反复调用除法
        print('乘除运算：',re_sub_expr)
        bb=com_chengchu(format_mark(re_sub_expr))
        return bb
def compute(express):
    express = com_chengchu(format_mark(express))
    express = com_jiajian(format_mark(express))
    return express
def delkuohao(express):
    #检测表达式是否存在括号，如果存在就去括号，否则直接执行
    res=re.compile(r'[()]')
    sub_expr1 = re.search('(\([\+\-\*\/\.0-9]+\))', express)
    if not sub_expr1:
        return express
    else:
        sub_expr1=sub_expr1.group()
        #delkuohao(express)
        #匹配括号，将计算结果替换到表达式
        sub_expr2=sub_expr1[1:len(sub_expr1)-1]
        sub_expr3=compute(sub_expr2)
        sub_expr3 = re.sub('(\([\+\-\*\/\.0-9]+\))', str(sub_expr3),express,count=1)
        print('括号运算：',sub_expr3)
        delkuohao_expr=delkuohao(format_mark(sub_expr3))
        return delkuohao_expr
if __name__=="__main__":
    #while True:
    #express=input("请输入要计算的表达式：")
    print('\n================================')
    print('\033[33m 混合运算计算器\033[0m')
    print('================================')
    #express ='1-2*((60-30+(-40.0/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
    while True:
        express = input('\033[32m请输入表达式,规范点哦 | (退出:q)\033[0m')
        express = re.sub('\s*', '', express)#0或多个表达式
        print(express)
        if len(express) == 0:
            continue
        elif express == 'q':
            sys.exit('退出程序')
        elif re.search('[^0-9\.\-\+\*\/\(\)]',express):
            print( '\033[31m 不是有效的算数表达式哦，请重新输入!!!\033[0m')
        else:
            express = express.replace(' ', '')
            print('您输入的表达式：',express)
            '''调用删除括号的函数'''
            express2 = delkuohao(express)
            #删除括号
            express2 = compute(format_mark(express2))
            #删除括号后再调用一次计算函数
            print('\033[31m表达式:%s'%express,'=', str(express2),'\033[0m')