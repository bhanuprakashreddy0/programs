def recursionfactorial(n):
    if n==1:
        return n
    else:
        return n*recursionfactorial(n-1)

number=int(input("enter the number:"))
if number<0:
    print("factorial doesnot exist")
elif number==0:
    print("the factorial for 0 is 1")
else:
    print('the factorial of',number,'is',recursionfactorial(number))
    
