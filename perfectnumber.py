number=float(input("enter the number:"))
sum=0
for i in range(1,number):
    if number%i==0:
        sum=sum+i
if sum == number:
    print("number is perfect number")
else:
     print("number is not a perfectnumber")
