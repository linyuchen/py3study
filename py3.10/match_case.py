from dataclasses import dataclass
res_status = 200

match res_status:
    case 200:
        print("res ok")
    case 401 | 403:
        print("not allowed")
    case 500:
        print("res internal 500")
    case _:
        print("others")

point = (0, 1)

match point:
    case (0, 1):
        print("point case")

point = (0, 1)
match point:
    case (x, 1):
        print(f"point {x=}")


@dataclass
class Point:
    x: int
    y: int


point = Point(x=0, y=1)
match point:
    case Point(x=0, y=1):
        print(f"{point=}")

match point:
    case Point(0, y):
        print(f"point {y=}")

point = [0, 1]
match point:
    case [0, _]:
        print(f"point=[0, ...]")

match point:
    case [0, _ as y] if y == 1:
        print(f"point 0, 1", f"{y=}")
