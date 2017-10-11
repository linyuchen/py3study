# -*- coding:UTF-8 -*-
from typing import List, Dict, Tuple, Callable, Mapping, Sequence, Type
__author__ = u"linyuchen"
__doc__ = u"""
类型提示功能
"""


def test_int(a: int) -> int:
    return a + 2

test_int(1)


def test_str(a: str) -> str:
    return "a" + a

test_str("2")


def test_float(a: float) -> float:
    return a + 0.1

test_float(1)


def test_list(a: List[int]) -> List[str]:
    a = map(str, a)
    return list(a)

print(test_list([1, "2"]))


def test_dict(a: Dict[str, int]) -> Dict[int, str]:
    return {a[k]: k for k in a}

print(test_dict({"1": 2}))


def test_tuple(a: Tuple[int, str]) -> None:
    print(a)

test_tuple((2, ""))
test_tuple((2, "", 2))


# Callable[[Arg1Type, Arg2Type], ReturnType]
def test_callable(a: Callable[[], str]) -> None:
    print(a())

test_callable(lambda: "1")


def test_callable2(a: Callable[[str], str]) -> None:
    print(a("callable"))

test_callable2(lambda a: a)


class ClassType:
    def instance_func(self):
        return "object func"

    @classmethod
    def class_func(cls):
        return "class func"


def test_object(a: ClassType) -> None:
    print(a.instance_func())

test_object(ClassType())


def test_type(a: Type[ClassType]) -> None:
    print(a.class_func())

test_type(ClassType)



