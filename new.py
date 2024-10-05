while True:
    print("\t\t\tWelcome to Menu\nSeelct Option\n1-Addition\n2-Substraction\n3-Multiplicatin\n4-Division\n5-Reminder\n6-Exponantial\n0-Exit\n")
    option=int(input())
    if(option==0):
        print("Exiting.....")
        break
    a=int(input("enter first number : "))
    b=int(input("enter second number : "))
    print("Result is : ",end="")
    if (option==1):
        print(a+b)
    elif (option==2):
        print(a-b)
    elif (option==3):
        print(a*b)
    elif (option==4):
        print(a/b)
    elif (option==5):
        print(a//b)
    elif (option==6):
        print(a**b)

