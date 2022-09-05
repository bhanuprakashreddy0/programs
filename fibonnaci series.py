numbers=int(input("how many numbers:"))
n1,n2=0,1
count=0
if (numbers<=0):
            print("no fibonnaci series for negative numbers")
elif numbers==1:
    print("fibonacci sequence upto",numbers,":")
    print(n1)
else:
    print("fibonacci sequence:")
    while count< numbers:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
