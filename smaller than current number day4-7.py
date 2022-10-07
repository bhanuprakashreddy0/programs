r=int(input("range of list:"))
l=[]
for i in range(r):
    i=int(input("enter:"))
    l.append(i)
print("numbers=",l)
m=l.copy()
def scnum(o):
    c=0
    for i in range(r):
        for j in range(r):
            if (l[i]!=m[j] and m[j]<l[i]):
                c=c+1
        print([c])
        c=0
scnum(r)
            
