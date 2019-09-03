#!/usr/local/bin/python3
def main():
    a="hello".upper()
    print("a is {0:>10} {1:>10}".format(a, 100))
    print(f"a is {a}")
    
if __name__ == "__main__":
    main()