#Inheritance: Concept in OOPs where child class inherits attributes and methods from parent class
#Single inheritance

class Grandparent:
    key="1234"
    def grandparent_method(self):
        return "Grandparent method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent method"

parent=Parent()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)