# -*- coding:UTF-8 -*-

__author__ = u"linyuchen"
__doc__ = u"""
系统调用中断时自动重试
"""

while True:
    try:
        print("Hello World")
        break
    except InterruptedError:
        continue

while True:
    try:
        data = file.read(size)
        break
    except InterruptedError:
        continue
