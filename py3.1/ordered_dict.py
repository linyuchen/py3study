# -*- coding:UTF-8 -*-
from collections import OrderedDict
__author__ = "linyuchen"
__doc__ = """
有序字典,
按照插入顺序排序，
插入已经存在的key，只会替换掉value，原来的位置不变
"""

d = OrderedDict()
d["a"] = "a"
d["1"] = "1"

print(d)
