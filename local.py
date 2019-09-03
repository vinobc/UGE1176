x = 10

def f():
    global x
    x = 20
    print(x)

f()
print(x)

del x
print(x)