def main():
    for i in range_all():
        print(i, end = " ")
    print()

def range_all(*args):
    begin = 0
    interval = 1
    length=len(args)
    if length < 1:
       raise TypeError(f"args is less than one. u passed {length}")
    if length == 1:
        end = args[0]
    if length == 2:
        (begin,end) = args
    if length == 3:
        (begin,end,interval)=args
    if length > 3:
       raise TypeError(f"too many args. u passed {length}")

    while begin <= end:
        yield begin
        begin += interval

if __name__ == "__main__":
    main()