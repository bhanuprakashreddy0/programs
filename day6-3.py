rows=int(input("enter the rows:"))
n=float(input("enter the strting number:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        
        print("%.1f"%n,end=" ")
        n=n+0.1
    print()
