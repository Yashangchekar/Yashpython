class Parentclass:
    def parent_method(self):
        print("This is parent method1")

    def yash(self):
        print("hello my name is yash")

class Childclass(Parentclass):
    # def parent_method(self):
    #     print("Harry")
    #     super().parent_method()


    def child_method(self):
        print("this is the child method2")
        # super().parent_method()
        super().yash()




child_object=Childclass()
child_object.child_method()
child_object.parent_method()
child_object.yash()

