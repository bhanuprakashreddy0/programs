a=int(input("enter the no of elements:"))
b=[]
for i in range(a):
    random_list=int(input("enter the numbers:"))
    b.append(random_list)
print("list of elements:",b)
frequency = {}
for item in b:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1
print(frequency)
