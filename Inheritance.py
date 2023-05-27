class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"the name of employee is {self.name}and id of employee{self.id}")

class Programmer(Employee): #---Inheritance



    def showlanguage(self):
        print(f"the default language is python{self.hero}")


a=Employee("rock",400)
a.showdetails()
a1=Employee("harry",600)
a1.showdetails()
a2=Programmer("monty",500) #Inheritance
a2.showdetails()
