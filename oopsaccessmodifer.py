class Employee: #public
    def __init__(self):
        self.name="Harry"
        self.__occ="engineer" #private

a=Employee()

print(a.name)
print(a._Employee__occ) #private can be accessed indirectly ((((((((((name mangling)))))))