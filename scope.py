def main():
    type = "hot"
    
    def mix_and_heat():
        print("prepare ingredients")
        print("heat milk/water in a bowl")
        print("put sugar")


    def make_coffee(param1):
        global type
        mix_and_heat()
        print("put coffee powder")
        coffee='{} coffee ready'.format(type)
        return coffee

    def make_tea():
        global type
        type = "cold"
        mix_and_heat()
        print("put tea powder")
        tea='{} tea ready'.format(type)
        return tea

    tea = make_tea()
    print(tea,"\n")
    coffee = make_coffee("cold")
    print(coffee)

if __name__ == "__main__":
    main()