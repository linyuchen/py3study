# -*- coding:UTF-8 -*-

__author__ = "linyuchen"
__doc__ = """
数字间可以加入下划线提高可读性
"""

a = 1_000
b = 0xFF_FF

print(a, b)

# 也可以直接在format里面加入下划线, 相当于千位分隔符
print('{:_}'.format(1000000))
