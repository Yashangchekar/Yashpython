tup=(1,5,63,7,5,9)
print(type(tup),tup)
tup1=(1,)
print(type(tup1))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1])
print(tup[1:3])

countries=("Spain","Italy","India","England","Germany")
print(countries)
temp=list(countries)
temp.append("russia") #add item

print(countries)      #remove item
print(temp)
temp.pop(3)
temp[2]="finland"
countries=tuple(temp)
print(countries)

countries2=("vietname","India","china")
gg=countries +countries2
print(gg)

tuple1=(0,2,3,4,5,32,5,)
r=tuple1.count(5)
r1=tuple1.index(5)
res1=tuple1.index(3,4,5)
print(res1)
print(r)
print(r1)
