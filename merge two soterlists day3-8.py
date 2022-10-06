first_list = []
second_list = []
count_first_list = int(input("Enter total numbers of the first list : "))
for i in range(1,count_first_list+1):
  no = int(input("Enter : "))
  first_list.append(no)
count_second_list = int(input("Enter total numbers of the second list : "))
for i in range(1,count_second_list+1):
  no = int(input("Enter : "))
  second_list.append(no)
print("First list : ",first_list)
print("Second list : ",second_list)
final_list = first_list + second_list
final_list.sort()
print("Final list : ",final_list)
