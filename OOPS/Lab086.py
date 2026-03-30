#Multilevel Inheritance


class Grandparent:
    key="1234"
    def grandparent_method(self):
        return "Grandparent method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent method"

class Child(Parent):
    def child_method(self):
        return "Child method"

parent=Parent()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)

child=Child()
print(child.child_method())
print(child.parent_method())
print(child.grandparent_method())
print(child.key)
