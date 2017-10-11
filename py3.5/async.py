# -*- coding:UTF-8 -*-
import types
__author__ = u"linyuchen"
__doc__ = u"""
async/await语法的异步协同
"""


@types.coroutine   # 装饰成一个协程
def wait():
    yield

async def f1():   # 返回一个awaitable对象
    print("1start")
    await wait()  # 除非再次调用send，否则后面的代码不会执行
    print("1end")

async def f2():
    print("2start")
    print("2end")


def run(f):
    try:
        f.send(None)
    except StopIteration:
        pass

f1 = f1()
f2 = f2()
run(f1)
run(f2)
run(f1)  # 继续执行
