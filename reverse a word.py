string=input("enter the string:")
reversedstring=""

index=len(string)
while index>0:
    reversedstring += string[index-1]
    index=index-1
print(reversedstring)
