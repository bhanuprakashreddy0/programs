def recursivefibonacci(n):
    if n<=1:
        return n
    else:
        return(recursivefibonacci(n-1)+recursivefibonacci(n-2))
nterms=int(input("enter the nterms:"))
           
if nterms<=1:
    print("invalid input")
else:
    print("fibonacci series:")
for i in range(nterms):
    print(recursivefibonacci(i))
        
