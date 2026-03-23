#Lambda Expression

def double_salary(salary):
    return salary * 2

new_salary=double_salary(100)
print(new_salary)

# Now will use lambda expression-useful for short one line operation
double_my_salary=lambda salary: salary * 2
print(double_my_salary(100))