a=[3,5,6,"list",True,6,7,2,32,345,23]
print(a)
print(a[1])
print(a[2])


print(a[-4]) #negative index
print(a[len(a)-3])
print(a[5-3])#positive index
print(a[2]) #positive index

if 7 in a:
    print("yes")
else:
    print("no")

if "ang" in "yashangchekar":
    print("yes")
else:
    print("no")
# a=[3,6,"list",True]
#a=[3,5,6,"list",True,6,7,2,32,345,23]
print(a)
print(a[1:])
print(a[1:-1])
print(a[1:8])
print(a[1:8:2])

lst=[i for i in range(4)]
print(lst)

lst=[i*i for i in range(10) if i%2==0]
print(lst)
b=[5,6,2,8,4,9,1,34]
print(b)
b.append(56)
print(b)
b.sort()
print(b)
b.reverse()
print(b)
print(b.index(2))
print(b)

c=b.copy()
print(c)
c.insert(1,100)
print(c)

m=[700,500,300]
b.extend(m)
print(b)

g=b+m
print(g)
