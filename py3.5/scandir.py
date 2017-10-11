# -*- coding:UTF-8 -*-
import os

__author__ = u"linyuchen"
__doc__ = u"""
os.scandir，更快的遍历目录，os.walk内部也用os.scandir实现了

返回的是个生成器
"""

for i in os.scandir("."):
    print(i, i.name, i.path, i.is_dir(), i.is_file())
