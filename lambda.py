# def double(x):
#     return x*2
double=lambda x:x*2
cube=lambda x: x*x*x
avg=lambda x,y:(x+y)/2
print(double(5))
print(cube(5))
print(avg(3,5))

def appl(fx,value):
    return 6 +fx(value)
print(appl(cube,2))

print(appl(lambda x:x*x*x,2))
print(appl(lambda x:x*x,2))

yash=lambda x,y,z:x+y+z
print(yash("yash","sanjay","angchekar"))


x="1"
y="2"
print(x+y)