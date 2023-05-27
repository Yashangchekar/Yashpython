import random

user=input("enter the key ")

moves=["rock","paper","scissor"]



cm=random.choice(moves)
if user=="rock":


    print(cm)
    if user==cm:
        print("both win draw")
    if user=="rock" and cm=="paper":
        print("computer wins")
    if user=="rock" and cm=="scissor":
        print("your win")

if user=="paper":
    print(cm)
    if user==cm:
        print("both win draw")
    if user=="paper" and cm=="scissor":
        print("computer wins")
    if user=="paper" and cm=="rock":
        print("your win")

if user=="scissor":
    print(cm)
    if user==cm:
        print("both win draw")
    if user=="scissor" and cm=="rock":
        print("computer wins")
    if user=="scissor" and cm=="paper":
        print("your win")
else:
    print("please enter correct statements")