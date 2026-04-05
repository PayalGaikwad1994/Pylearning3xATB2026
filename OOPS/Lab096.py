#Exception-Event that occurs during execution of program that disrupts flow of instructions
#Exception handling: when an error occurs, instead of crashing the program, we catch and handle it



try:
    numA=int(input("Enter a number: "))
    numB=int(input("Enter another number: "))
    div=numA/numB

except Exception as e:
    print(e)
    print("Please enter a number!")
else:
    print("Division is",div)

finally:
    print("Anyway I will be executing")
