def main():
    # x = dict({"a":1, "b":33})
    # x = dict(a = 10, b = "hello")
    # a(**x)

    a(a = 23, b = "hello")
    
def a(**kwargs):
    for k in kwargs:
        print(k,kwargs[k])

if __name__ == "__main__":
    main()