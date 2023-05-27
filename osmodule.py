import os
print(dir(os))
# os.mkdir("data")
for i in range(0,20):
    print(os.mkdir(f"data1{i+1}"))