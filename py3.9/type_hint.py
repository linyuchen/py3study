# 标准类型可直接用于标注


a: list[int] = [1, 2]  # 不需要像以前 from typing import List，现在直接使用list或者dict之类的标准类型


def func() -> dict:
    return {}

