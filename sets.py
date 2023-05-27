

se={2,4,5,6,6,7,8,9,7}# not in order
print(type(se))
print(se)

info1={"carla",19,False,5.9,19}
print(info1)
print(type(info1))


s1={1,2,5,6}
s2={3,5,7}
print(s1.union(s2))
s1.update(s2)

cities={"tokyo","Madrid","berlin","Delhi"}
cities2={"tokyo","Seoul","kabul","Madrid"}
cities3=cities.intersection(cities2)
print(cities3)


cities.intersection_update(cities2)
print(cities)
cities4=cities.symmetric_difference(cities2)
print(cities4)

cities3=cities.difference(cities2)
print(cities3)

cities6=cities.isdisjoint(cities2)
print(cities6)
cities7=cities.issuperset(cities2)
print(cities7)
cities.add("mumbai")
print(cities)