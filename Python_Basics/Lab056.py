#tuple and list

mylist=[]
mylist.extend([2,3,3,5,6])
print(mylist)

mytuple=(6,7,8,9,"Maya")
print(mytuple)

t = (1, 2, 3)
print(id(t))
t = t + (4, 5)
print(t)
print(id(t))

t = (1)
print(type(t))

#To create a single-element tuple:
t1 = (1,)
print(type(t1))
print(t1)

t2  =tuple()
print(type(t2))
print(t2)

t3=tuple(["mm",2,3])
print(t3)
print(type(t3))

