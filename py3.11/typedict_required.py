from typing import TypedDict, NotRequired, Required


class Test(TypedDict):
    a: NotRequired[str]
    b: Required[str]


test: Test = {"a": "a"}  # Type error, missing key b
test2: Test = {"b": "b"}  # is ok
