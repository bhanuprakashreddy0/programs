totalusers=int(input("enter the total users:"))
staffusers=int(input("enter staff users:"))
nonteachingstaff=staffusers//3
staffusers=nonteachingstaff+staffusers
studentusers=totalusers-staffusers
print("studentusers:",studentusers)
