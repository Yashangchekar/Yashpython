class person:#class
    name="harry"
    occupation="Software development"
    networth=10
    def info(self):
        print(f"{self.name}is a {self.occupation}")
a=person()#a=object
b=person()#b=object
c=person()#c=object
a.name="yash"
a.occupation="bioinformatics"
b.name="rokan"
b.occupation="clerk"
print(a.name,a.occupation)
a.info()
b.info()
c.info()