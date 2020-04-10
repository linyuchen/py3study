#-*- coding:utf8 -*-

from dataclasses import dataclass


@dataclass
class Test:
    name: str = ""  # 这里要加上类型注解 直接name = ""是不行的
    age: int = 0


if __name__ == "__main__":
    t = Test(name="jojo", age=13)
    print(t.name, t.age)
