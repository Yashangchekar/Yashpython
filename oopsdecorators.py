def greet(fx):
    def mfx(): #if you use interger valaule definedit with *args **kwargs  inside mfx
        print("good morning")
        fx() #key of decorator (integar value define *args **kwargs

        print("Thanks for using this function")

    return mfx


@greet #decorators
def hello():
    print("hello world")

def add(a,b):
    print(a+b)
hello() # greet(hello)() another way to do it
add(3,5)#greet(add)(1,2)