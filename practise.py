class Person:

    def __init__(self,r,m):
        print("hey this on is default constructor")
        self.rock=r
        self.malle=m

    def info(self):
        print(f"{self.rock} is a {self.malle}")
a=Person("jinder","cage")
a.info()
