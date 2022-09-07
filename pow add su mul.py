def add(x,y):
    c=x+y
    return c
def sub(x,y):
    c=x-y
    return c
def mul(x,y):
    c=x*y
    return c
def div(x,y):
    c=x/y
    return c
def pow(x,y):
    c=x**y
    return c
while True:
    a=float(input("enter the first number:"))
    b=float(input("enter the second number:"))
    cal=input("eneter the choice[+,-,*,/,**]")
    if cal=='+':
        print("the added value:",add(a,b))
    elif cal=='-':
        print("the subtracted value:",sub(a,b))
    elif cal=='*':
        print("the multiplicated value:",mul(a,b))
    elif cal=='/':
        print("the divided value:",div(a,b))
    elif cal=='**':
        print("the power value:",pow(a,b))
    else:
        print("invalid input")
