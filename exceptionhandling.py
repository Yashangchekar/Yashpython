a=input("Enter the number")
print(f"Multiplication table of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)})x {i}={int(a)*i}")
except:
    print("invalid input")


try:
    num=int(input("enter the integer"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("number entered is not a integer")