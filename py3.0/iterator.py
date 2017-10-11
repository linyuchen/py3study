# -*- coding:UTF-8 -*-

__author__ = u"linyuchen"
__doc__ = u"""
一些函数不再返回列表，而是返回了迭代器
迭代器更加节约内存，速度也更快


dict方法:
    dict.keys()，dict.items(), dict.values() 返回迭代器

    删除的方法: dict.iterkeys()，dict.iteritems(), dict.itervalues()

map(), filter()返回迭代器。

range()代替了xrange(), 并且返回迭代器

zip()返回迭代器。
"""