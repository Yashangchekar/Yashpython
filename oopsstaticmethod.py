class Math:
    def __init__(self,num):
        self.num=num

    def addtosum(self,n):
        self.num=self.num+n

    @staticmethod  #@staticmethod
    def add(a,b):   #@staticmethod
        return a+b


a=Math(5)
print(a.num)
a.addtosum(6)
print(a.num)
print(a.add(7,2)) #@staticmethod
# print(add(4,5)) @staticmethod