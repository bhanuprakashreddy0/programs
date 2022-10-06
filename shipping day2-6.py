a=int(input("enter number of items:"))
def cost(x):
    if(x<0):
        print("enter only positive numbers.")
    elif x==1:
        print(750)
    else:
        print(750+(x-1)*200)
cost(a)
