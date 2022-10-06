a=int(input("enter the no. of elements:"))
b=[]
for i in range(0,a):
     c=int(input("enter the elements:"))
     b.append(c)
print("list of elements:",b)
max=int(input("max="))
min=int(input("min="))
if(max <=0 or min<=0):
  print("invalid input")
else:
  b.sort()
  for i in range(0,a):
     if (min-1==i):
       d=b[i]
  b.reverse()
  for i in range(0,a):
      if(max-1==i):
         e=b[i]
  print("sum =",e+d)
  print("difference=",e-d)
  
