# -*- coding:UTF-8 -*-

__author__ = u"linyuchen"
__doc__ = u"""
解构/解包
"""

# *解包, 相当于把数组或者列表外面的"()"或者"[]"去掉
a = range(3)
print(*a)  # 等同于print(0, 1, 2)

# **解包, 解包字典时，相当于把"{}"去掉
d = {"a": "a", **{"b": "b"}}  # 等同于{"a": "a", "b": "b"}
print(d)
