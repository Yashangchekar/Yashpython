f=open('mydoc.txt')
while True:
    line=f.readline()
    # print(line)
    if not line:
        break
    print(line,type(line))
