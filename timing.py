import time

x=int(input("enter the value of x:"))

match x:
    case 0:
        print("x is zero")

    case 4:
        print("case is 4 ")

    case _ if x==90:
        print(x,"is  90")

    case _ if x==80:
        print(x," is  80")

    case _:
        print(x)