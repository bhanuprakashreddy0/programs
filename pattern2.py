rows=int(input("enter the rows:"))
k=2*rows-2
for i in range(1,rows):
    for j in range(1,k):
        print(end="")
    k=k-2
    for j in range(1,i+1):
        print(i,end="")
    print("\r")
