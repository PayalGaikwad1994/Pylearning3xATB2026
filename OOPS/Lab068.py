#filter: built-in function allows you to filter elements in the list

numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)

def iseven(num):
    return num % 2 == 0

def is_greater_than_5(num):
    return num > 5

even_numbers=filter(iseven,numbers)
print(list(even_numbers))

number_greater_5=filter(is_greater_than_5,numbers)
print(list(number_greater_5))