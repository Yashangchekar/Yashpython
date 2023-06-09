class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"

    def __add__(self,x):
        return f"{self.i+x.i}i+{self.j+x.j}i+{self.k+x.k}k"

v=vector(2,4,6)
print(v)
v1=vector(4,5,6)
print(v1)
print(v1+v)