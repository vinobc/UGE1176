def main():
    # ingredients = ("hot","lemon","without sugar", 100, 20)
    tea = make_tea("hot","lemon","without sugar")
    # tea = make_tea(* ingredients)


    print(tea, "\n")
    coffee = make_coffee("Cold", "hot")
    print(coffee)

def mix_and_heat():
	print("prepare ingredients")
	print("heat milk/water in a bowl")
	print("put sugar")


def make_coffee(param1, p2=0):
	mix_and_heat()
	print("put coffee powder")
	coffee='{} {} coffee ready'.format(param1, p2)
	return coffee

def make_tea(*args):
	mix_and_heat()
	print("put tea powder")
	tea='tea ready with {} ingredients'.format(len(args))
	return tea

if __name__ == "__main__":
    main()