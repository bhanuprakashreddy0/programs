rows=int(input("enter the no of rows:"))
columns=int(input("enter the no of columns:"))
for i in range(rows):
    for j in range(columns):
        print('*',end="")
    print("\r")
