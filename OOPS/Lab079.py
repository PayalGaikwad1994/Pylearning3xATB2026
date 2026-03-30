#Encapsulation: Bind data variables with methods
#Hide data members by using only methods
#data member value should change only by class methods

class Car:
    name=None

    def __init__(self):
        self.public_var="Public Var"
        self._protected_var="Protected Var"
        self.__private_var="Private Var"

    def __privateMethod(self):
       print("Private Method")

    def printName(self):
        self.privateMethod()
        if self.__private_var=="1234":
            print("Private variable accesses")
        print("I am allowed to Picnic")


alto=Car()
print(alto.name)
print(alto.public_var)