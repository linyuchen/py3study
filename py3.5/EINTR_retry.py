# -*- coding:UTF-8 -*-

__author__ = "linyuchen"
__doc__ = """
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
