# -*- coding:utf8 -*-

print("1")
breakpoint()  # 进入pdb调试模式，可利用pdb命令调试
print("2")


"""
                pdb调试命令

完整命令	简写命令	描述

args	        a	        打印当前函数的参数
break	        b	        设置断点
clear	        cl	        清除断点
condition	无	        设置条件断点
continue	c或者cont	继续运行，知道遇到断点或者脚本结束
disable	        无	        禁用断点
enable	        无	        启用断点
help	        h	        查看pdb帮助
ignore	        无	        忽略断点
jump	        j	        跳转到指定行数运行
list	        l	        列出脚本清单
next	        n	        执行下条语句，遇到函数不进入其内部
p	        p	        打印变量值，也可以用print
quit	        q	        退出 pdb
return	        r	        一直运行到函数返回
tbreak	        无	        设置临时断点，断点只中断一次
step	        s	        执行下一条语句，遇到函数进入其内部
where	        w	        查看所在的位置
!	        无	        在pdb中执行语句
"""
