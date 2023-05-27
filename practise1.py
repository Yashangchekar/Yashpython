import time

a=int(time.strftime('%H'))
print((a))

if a<12:
    print("gm")
elif a>=12 and 15<=a:
    print("ga ")

else:
    print("gn")