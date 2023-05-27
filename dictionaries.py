dic={"harray":1,"Yash":2,"sanjay":3}
print(dic["harray"])
print(dic.get("Yash"))
print(dic.values())

for key in dic.keys():
    print(dic[key])

ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:90}
ep1.update(ep2)

print(ep1)
ep1.popitem()
print(ep1)
del ep1[122]
print(ep1)