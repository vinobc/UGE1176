#!/usr/local/bin/python3
def main(i):
    if i == 0:
        print("we are done..")
        return
        
    else:
        print(i,"..")
        main(i-1)
        print(i,"hello")
    

if __name__ == "__main__":
    main(5)