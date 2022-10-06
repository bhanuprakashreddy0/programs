rows=int(input("enter number of rows:"))
coef=1
for i in range(1,rows+1):
    for k in range(1,rows-i+1):
        print(" ",end="")
    for j in range(0,i):
        if j==0 or i==0:
            coef=1
        else:
            coef=coef*(i-j)//j
        print(coef,end=" ")
    print()
def calculatesum(n):
    sum=1
    
    for row in range(1,n):
        sum=sum+(1<<row)
    return sum
n=int(input("enter the row number:"))
print("sum of all elements in ",n," row is:",calculatesum(n))
