
t1=[]
t2=[]
a=int(input("enter the range of list1:"))
print("enter the elemnts of list1")
for i in range(a):
    x=int(input())
    t1.append(x)
b=int(input("list2 range"))
print("enter the elements in list2")
for j in range(b):
    y=int(input())
    t2.append(y)
res=sorted(t1+t2)
print("the combined list"+str(res))
