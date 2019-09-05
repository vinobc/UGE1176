def main():
    i = [10]
    a(i)
    print(i)

def a(j):
    # print(id(j))
    j[0] = 20
    # print(id(j))
    print(j)

if __name__ == "__main__":
    main()