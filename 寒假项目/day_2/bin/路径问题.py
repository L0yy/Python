#!/usr/bin/env python
# Auther:Cray
# -*- coding:utf-8 -*-
import os
import sys

Base=os.path.dirname(os.path.dirname(__file__))
sys.path.append(Base)
print(Base)
from conf import test2
test2.code()
print(__file__)