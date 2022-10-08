age=int(input("enter your age:"))
if(age>=18):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
    remaining=18-age
    print("You are allowed to vote after",remaining,"years.")
