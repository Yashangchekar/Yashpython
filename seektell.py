with open('mydoc.txt','r')as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data=f.read(5)
    print(data)

with open('mydoc.txt','w')as f:
    f.write('helloworld')
    f.truncate(5)