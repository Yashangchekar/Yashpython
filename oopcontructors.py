class Person:

    # def __init__(self):
    #     print("hey this on is default constructor")---------------default contructor with no parameter
    def __init__(self,n,o):
        print("hey how are you")
        self.name=n
        self.occ=o

    def info(self):
        print(f"{self.name}is a {self.occ}")
a=Person("keshav","worker")
a.info()
b=Person("Pankaj","robbery")
b.info()