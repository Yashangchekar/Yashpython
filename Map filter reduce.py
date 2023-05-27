def cube(x):
    return x*x*x
print(cube(2))
l=[1,2,4,6,4,3]
newl=list((map(cube,l)))
print(newl)

#eg map function
numbers=[1,2,3,4,5]
double=map(lambda x:x*2,numbers)
print(list(double))

def yash(x):
    return x+x+x
print(yash(1))
c=[1,2,3,4,5]
new=list(map(yash,c))
print(new)
#/////////////////
#filter funtion

def filter_function(a):
    return a>4
l1=[2,4,2,5,7,8,9]
newnewl=list(filter(filter_function,l1))


print(newnewl)

#reduce
from functools import reduce
numbers1=[1,2,3,4,5]
def sum(x,y):
    return x+y
sum=reduce(sum,numbers1)
print(sum)

