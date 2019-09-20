import time
def duration(fn):
    def inner():
        begin = time.time()
        fn()
        end = time.time()
        print(f"Compute duration: {(end-begin)} secs.")
    return inner

@duration
def main():
    values = []
    # begin = int(input("min"))
    # end = int(input("max"))
    for value in range(1,200000):
        values.append(value)
    print(f"Sum of numbers from min to max is:{sum(values)}")

if __name__ == "__main__":
    main()