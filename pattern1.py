rows=int(input("enter the rows:"))
for i in range(1,rows):
    for j in range(1,i+1):
        print(i,end="")
    print("\r")
