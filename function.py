def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
    if (a>b):
        print("first number is great which is :",a)
    else:
        print("second number is great which is ",b)
calculateGmean(10,9)


def evenodd(a):

    if a%2==0:
        print("this is even number",a)
    else:
        print("this is odd ")
evenodd(int(input("enter the number")))

def hello(a,b,c):
    pass

def average(a=10,b=2):
    print("average is ",(a+b)/2)

average(3,5)


def average(*numbers): #tuple
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is ",sum/len(numbers))
average(5,6)



def name(**name): #dictonary
    print("hello",name["fname"],name["mname"],name["lname"])

name(mname="Buchanan",lname="barnes",fname="james")

def add(a=4,b=4):
    sum=a+b
    return sum
