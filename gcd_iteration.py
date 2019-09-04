#!/usr/local/bin/python3
def main(x,y):
    while(y != 0):
        x_holder = x
        x = y
        y = x_holder % y
    print(x)

if __name__ == "__main__":
    main(54,24)