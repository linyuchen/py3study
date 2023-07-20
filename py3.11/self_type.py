from typing import Self


class MyClass:
    @classmethod
    def get_class(cls) -> Self:
        return MyClass()

