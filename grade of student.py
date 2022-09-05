physics=int(input("enter the marks in physics:"))
maths=int(input("enter the marks in maths:"))
science=int(input("enter the marks in science:"))
total=physics+maths+science
print("total:",total)
avg=total/300*100
if(avg>90):
    print("A Grade")
elif(avg<=90 == avg>75):
    print("B Grade")
elif(avg<=75 == avg>60):
    print("C grade")
else:
    print("F")

    
