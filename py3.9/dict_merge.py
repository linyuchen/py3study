a = {"a": "a"}
b = {"b": "b"}

print(a | b)  # 输出{'a': 'a', 'b': 'b'}

# 也可以直接表达式赋值
a |= b
print(a)  # 输出{'a': 'a', 'b': 'b'}
