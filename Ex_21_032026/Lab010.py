#String functions

str="gaikwaD"
print(str)
print(type(str))
print(id(str))
print(len(str))
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.title())
print(str.center(15,'*')) #The center() method returns a new centered string after padding it with the specified character.
str=str.upper()
print(str)
print(id(str))
#str[0]="H" #TypeError: 'str' object does not support item assignment
print(str[15]) #IndexError: string index out of range