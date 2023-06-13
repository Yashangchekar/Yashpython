print("Hybrid Inheritence")

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")

class cat1(Animal):
    def __init__(self, name, breed, species1="cat"):
        Animal.__init__(self, name, species1)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class cat2(Animal):
    def __init__(self, name, breed, species2="cat1"):
        Animal.__init__(self, name, species2)
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class finalcat3(cat1,cat2):
    def __init__(self,name,breed,species1="cat",species2="cat1"):

        cat1.__init__(self,name,breed,species1)
        cat2.__init__(self,name,breed,species2)
        self.breed=breed

    def show_details(self):
        cat1.show_details(self)
        cat2.show_details(self)


a=finalcat3("yash","kkk")
a.show_details()

