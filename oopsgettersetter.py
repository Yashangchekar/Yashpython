class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")

    @property #-----getter
    def Ten_value(self):
        return 10*self._value


obj=Myclass(10)

print(obj.Ten_value)
obj.show()