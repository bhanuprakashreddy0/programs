h=int(input("enter the starting range:"))
l=int(input("enter the ending range:"))
if(h<=0 or h<=l):
    print("Invalid input.")
else:
    for i in range(h,l+1):
        count=0
        for divider in range(2,i//2+1):
            if(i%divider==0):
                count+=1
        if(count>=1):
            print(i)
