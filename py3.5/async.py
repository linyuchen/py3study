# -*- coding:UTF-8 -*-
import asyncio

__author__ = "linyuchen"
__doc__ = """
async/await语法的异步协同
"""

import time


# 定义一个协程函数
async def async_func():
    print("async_func")


# 在协程函数中运行另外个协程函数
async def async_func2():
    await async_func()  # 等待async_func运行完毕
    print("async_func2")


asyncio.run(async_func2())


async def gather_func():
    await asyncio.sleep(1)
    print("gather_func")


async def gather_func2():
    await asyncio.sleep(1)
    print("gather_func2")


# 并发运行多个协程函数
async def gather_run():
    # 可以看到gather_func和gather_func2是同时运行的，并不会等待前一个运行完毕再运行
    await asyncio.gather(gather_func(), gather_func2())


asyncio.run(gather_run())


def sync_func():
    time.sleep(1)
    print("sync_func")


# 在异步函数中运行同步函数
async def run_sync_func():
    await asyncio.to_thread(sync_func)


asyncio.run(run_sync_func())
