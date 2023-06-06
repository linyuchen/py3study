def func(a: int | str):
    print(a)


func(1)
func("2")

print(isinstance(1, str | int))