try:
    number=int(input("enter the number:"))
    reversenumber=0
    while number>0:
        remainder=number%10
        reversenumber=reversenumber*10+remainder
        number=number//10
    print(reversenumber)
except ValueError:
    print("enter the input as integers only")
    
    
