
import time
def usingWhile(i):
    i=0
    while i<50000:
        i=i+1
        print(i)
def usingfor():
    for i in range(5000):
        print(i)

# init=time.time()
# usingfor()
# print(time.time()- init)
# init=time.time()
# usingWhile()
# print(time.time()- init)

print(4)
time.sleep(4)

y=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H-%M-%S",y)
print(formatted_time)



