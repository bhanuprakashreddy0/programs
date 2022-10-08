try:
    n=int(input("enter the no of rows:"))
    if(n<=0):
        print("Inavalid input")
    else:
        for i in range(n+1):
            for j in range(1,i+1):
                print(j/10,end=" ")
            print("\n")
except ValueError:
    print("please enter only integers.")
