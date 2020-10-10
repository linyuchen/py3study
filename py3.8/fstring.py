# f-string新增=扩展表达式，将变量的值直接表达出来

a = "I'm a"

print(f"{a=}")  # 输出a="I'm a"

# 等价于
print(f'a="{a}"')
