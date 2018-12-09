#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import os
data=input('请输入命令>>:').strip()
cmd_res= os.popen(data,'r').strip()
print(cmd_res)