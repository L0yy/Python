#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
# try:
#     a=['a','v']
#     print(a[3])
# except Exception as yy:
#     print(yy)


# s1 = 'hello'
# try:
#     int(s1)
# except IndexError as e:
#     print(e,'\n')
# except KeyError as e:
#     print(e,'\n')
# except ValueError as e:
#     print(e,'\n')
# #except Exception as e:
# #    print(e)
# else:
#     print('try内代码块没有异常则执行我')
# finally:
#     print('无论异常与否,都会执行该模块,通常是进行清理工作')


class WupeiqiException(Exception):
    def __init__(self, msg):
        self.message = msg

    def __str__(self):
        return self.message


try:
    raise WupeiqiException('我的异常')#主动触发异常
except WupeiqiException as e:
    print(e)
