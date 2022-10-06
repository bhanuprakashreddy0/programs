def interest(p,y,s):
  if(s=='yes'):
    SI=int((p*y*12)/100)
  else:
    SI=int((p*y*10)/100)
  return SI
p=int(input("Enter the Amount :"))
y=int(input("Enter the number of years:"))
senior=input("Are you Senior Citizen (yes/no):")
print("Your Interest is :",interest(p,y,senior))
