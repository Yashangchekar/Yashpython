def factorial(n):
    if(n==0 or n==1):
        return 1
    else:

        return n * factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))


def fibonacci(n):
    if n<=1:
        return n
    else:
        return factorial(n-1)+fibonacci(n-2)

for i in range(10):
    print(fibonacci(i))

