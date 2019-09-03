def main():
    a,b = 20,10

    # if a < b:
    #     print("a is less than b")
    # elif a > b:
    #     print("a is greater than b")
    # else:
    #     print("a is equal to b")

    res = "a is less than b" if (a < b) else "a is greater than or equal to b"
    print(res)

if __name__ == "__main__":
    main()
    