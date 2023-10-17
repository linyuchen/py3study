# 简要的学习一下Python3必须知道的新特性

## Python3.0

* [print函数](py3.0/print.py)
* [Unicode大统一，不再担心各种编码问题](py3.0/str.py)
* [迭代器](py3.0/iterator.py)


## Python3.1

* [新增序列计数类Counter](py3.1/counter.py)
* [字符串和数字的format](py3.1/format.py)
* [有序的字典](py3.1/ordered_dict.py)


## Python3.2

* [命令行解析模块argparse](py3.2/args_parser.py)

## Python3.3

* [自带虚拟环境模块venv](py3.3/venv.md)


## Python3.4

* 没有新的语法特性，大部分是一些bug的修复
* 还有一些新增的模块，平时没有怎么用到的说

## Python3.5

这是革命性的一个版本啊

* [语法上支持协程, async await](py3.5/async.py)
* [支持byte类型的格式化操作](py3.5/byte_format.py)
* [系统调用中断信号时，可以自动重试](py3.5/EINTR_retry.py)
* [math新增判断近似相等方法isclose](py3.5/isclose.py)
* [矩阵相乘操作符@](py3.5/matrix_multiplication.py)
* [更快的遍历目录 os.scandir](py3.5/scandir.py)
* [解包操作](py3.5/unpacking.py)
* [把压缩包当做模块直接运行](py3.5/zipapp.md)
* [类型提示功能](py3.5/type_hint.py)

## Python3.6

* [数字间加入下划线，提高数字可读性](py3.6/int_.py)
* [字符串字面量语法](py3.6/strformat.py)

* [变量支持类型提示](py3.6/var_type.py)

## Python3.7

* [dataclass，更方便的初始化类成员](py3.7/dataclass.py)

* [内置breakpoint()函数，自带pdb调试](py3.7/breakpoint.py)
* dict对象会保持插入时的顺序


## Python3.8

* [:=, 表达式直接赋值](py3.8/assignment_expressions.py)

* [仅限位置形参](py3.8/positional_only_parameters.py)

* [f-string中直接用=输出变量值](py3.8/fstring.py)


## Python3.9

* [dict增加合并运算符 |](py3.9/dict_merge.py)

* [类型注解支持内置的标准类型，如list和dict](py3.9/type_hint.py)

* [str增加removeprefix和removesuffix方法](py3.9/str_remove_pre_suf.py)


## Python3.10

* [比if else更好用的匹配模式match case](py3.10/match_case.py)

* [新的联合类型运算符 |](py3.10/new_union.py)

## Python3.11

* [TypeDict新增可选和必须](py3.11/typedict_required.py)
 
* [typing新增Self，表示类实例本身](py3.11/self_type.py)
 
* [新增库tomllib，用于处理toml格式文件](py3.11/toml.py)

* [enum新增StrEnum，用于限制枚举值为字符串](py3.11/str_enum.py)

更多详情见[官网](https://docs.python.org/zh-cn/3/)