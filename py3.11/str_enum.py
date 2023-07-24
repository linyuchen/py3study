from enum import StrEnum, Enum


class TestStrEnum(StrEnum):
    a = "a"


class TestEnum(Enum):
    a = "a"


print(TestStrEnum.a, (TestStrEnum.a == "a"))
print(TestEnum.a, (TestEnum.a == "a"))


