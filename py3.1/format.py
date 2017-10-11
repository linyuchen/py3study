# -*- coding:UTF-8 -*-

__author__ = u"linyuchen"
__doc__ = u"""
内建函数format
str.format支持自动编号
"""


print(format(123444, ",d"))  # 10进制，千位分隔符
print(format(123444, "o"))  # 8进制
print(format(123444, ".2f"))  # 保留小数位
print(format(123444, ",.2f"))  # 千位分隔符并保留小数位


print("{0},{1}".format("1", "2"))
# str.format支持自动编号
# 效果同上
print("{},{}".format("1", "2"))
