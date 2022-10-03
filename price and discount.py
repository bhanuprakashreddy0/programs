try:
    freshloaves=int(input("enter the no of freshloaves:"))
    oldloaves=int(input("enter the no of oldloaves:"))
    price=(freshloaves*185)
    price1=oldloaves*185*.6

    print("amount of reshloaves:",price)
    print("amount of old leaves",price1)
    print("total price is:",price+price1)
except ValueError:
    print("enter the positive amnumber without decimal")
