#!/usr/bin/env python
# __Auth0r__:Cray
# -*- coding:utf-8 -*-
import hashlib
while True:
    text=input(">>:").strip().encode()
    a=hashlib.md5(text).hexdigest()
    print(a)
