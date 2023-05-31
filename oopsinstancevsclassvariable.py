class Employees:
    companyName="apple" #class variable
    numberofemployees=0
    def __init__(self,name):
        self.name=name         #instancevariable
        self.raise_amount=0.02
        Employees.numberofemployees +=1
    def showdetails(self):
        print(f" the name of the Employees is {self.name} and raise amount is {self.raise_amount}and {self.companyName}"
              f" employees number is  {self.numberofemployees}")

emp1=Employees("harry")
emp1.raise_amount=00.3  #instance variable
emp1.companyName="apple india" #instance variable
emp1.showdetails()
emp2=Employees("rogan")
emp2.showdetails()
# Employees.showdetails(emp1)