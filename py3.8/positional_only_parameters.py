# 仅限位置形参：将参数表明只能通过位置传参，不能是关键字传参


def func(a, b, /):  # 在位置形参后加上/表明仅限位置形参
    print(a, b)


# 只能这种方式传参
func(1, 2)

# func函数的参数a, b就不能是a=xx,b=xx的形式传入了
func(a=1, b=2)  # 关键字传参会直接报错


def func2(a, b, /, c=3, **d):
    print(a, b, c, d)


func2(1, 2, c=4)
