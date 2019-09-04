#!/usr/local/bin/python3
def main():
    color = input("What is my favorite color?")

    if color == "green":
        print("You guessed right..")
    else:
        print("That's not my fav. color..")
    
    print("Thanks for playing !!")
    
    response = input("continue(y/n)")
    if response == "y":
        main()
    else:
        return
    

if __name__ == "__main__":
    main()