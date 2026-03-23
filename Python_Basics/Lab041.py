# Function example

#No statements will be executed after return statement
def myfunction3(num1, num2):
    return num1 + num2
    print("This will not getting executed")

print(myfunction3(1, 2))
#print(myfunction3()) #TypeError: myfunction3() missing 2 required positional arguments: 'num1' and 'num2'