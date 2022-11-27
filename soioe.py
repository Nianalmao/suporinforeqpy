x=int(input("x="))
y=int(input("y="))
if (x>y):
    print(x,end="")
    print("is superior to", end="")
    print(y)
elif (x<y):
    print(x,end="")
    print("is inferior to", end="")
    print(y)
else:
    print(x,end="")
    print("equals", end="")
    print(y)