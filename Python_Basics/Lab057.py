#Tuples and Decorators

#real Case where tuples use

API_URLs=("https://courses.thetestingacademy.com/","https://awesomeqa.com/","https://courses.thetestingacademy.com/courses")
print(API_URLs[0])
print(API_URLs[1])
print(API_URLs[2])

t=()
print(type(t))
print(t)

t1=tuple()
print(type(t1))
print(t1)

t2=tuple(["Meena",1,True,False,12.4])
print(type(t2))
print(t2)

del t #to delete tuple