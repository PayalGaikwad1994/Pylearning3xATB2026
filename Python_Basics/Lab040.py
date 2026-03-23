# Functions

# function with no arguments and no return type
def myfunction():
    print("Hi")


# function with argument and no return type
def myfunction1(name):
    print("Hi", name)


# function with argument and no return type
def myfunction2(name="Poyal"):
    print("Hi", name)


# function with argument and return type
def myfunction3(num1, num2):
    return num1 + num2


myfunction()
myfunction1("Piha")
myfunction2()
myfunction2("BR")
result = myfunction3(6, 7)
print(result)
