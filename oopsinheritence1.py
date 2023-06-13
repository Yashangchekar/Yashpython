class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(selfs):
        print("sound made by the animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def make_sound(selfs):
        print("Barks")

a=Dog("Yash","Doggerman")
a.make_sound()
a=Animal("kkk","MMM")
a.make_sound()

#mutiple inheritence
class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"the name is {self.name}")


class Dancer:
    def __init__(self, Dance):
        self.Dance = Dance

    def show(self):
        print(f"the Dance is {self.Dance}")

class DancerEmployee(Employee,Dancer):
    def __init__(self, name, Dance):
        self.name = name
        self.Dance =Dance

o=DancerEmployee("shivani","kathak")
print(o.name)
print(o.Dance)

print(DancerEmployee.mro())

o.show()


