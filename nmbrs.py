#!/usr/local/bin/python3
from decimal import Decimal
def main():
    x = Decimal(".20")
    y = Decimal(".60")
    a = x + x + x - y
    print(f"a is {a}")
    print(type(a))
    # b = 10/3
    # print(f"b is {b}")
    # print(type(b))
    # c = 10//3
    # print(f"c is {c}")
    # print(type(c))
    # d = 10**3
    # print(f"d is {d}")
    # print(type(d))
    
if __name__ == "__main__":
    main()