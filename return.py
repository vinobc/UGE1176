def main():
    result = a()
    print(type(result), result)
    
def a():
    print("hello")
    # return "return from function 'a'."
    return dict(a=100, b="tiger")

if __name__ == "__main__":
    main()