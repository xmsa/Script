#! /usr/bin/python
import sys


def to_goedel_number(x, y):
    z = (2**x) * (2*y + 1)
    return max(z-1, 0)


def goedel_number_to(z):
    z += 1
    x = 0
    while z % 2 == 0:
        z = z // 2
        x += 1
    y = (z-1) // 2
    return x, y


if __name__ == "__main__":
    if len(sys.argv) == 2:
        z = int(sys.argv[1])
        print(goedel_number_to(z))

    elif len(sys.argv) == 3:
        x, y = int(sys.argv[1]), int(sys.argv[2])
        print(to_goedel_number(x, y))

    else:
        print("encoding <x,y>:z : python goedel_number.py x y")
        print("decoding z:<x,y> : python goedel_number.py z")
