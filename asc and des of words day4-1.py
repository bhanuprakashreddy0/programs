string=int(input("enter the no of words:"))
b=[]
for i in range (string):
    c=input("enter the words:")
    b.append(c)
print("list of words:",b)
print("ascending order:")
b.sort()
print(b)
c=b
print("descending order:")
c.reverse()
print(c)
      
