#Example of Lambda Expression

def sum_numbers(num1,num2):
    return num1+num2

print(sum_numbers(10,20))

#Now will use lamda
sum_num=lambda a,b: a+b
print(sum_num(10,20))