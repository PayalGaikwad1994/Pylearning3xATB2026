#list in Python
#A list is a mutable, ordered collection of elements.
#Key Properties
#Ordered ✅
#Mutable ✅ (can change)
#Allows duplicates ✅
#Can store different data types ✅

mylist=["Payal",12,34,"",23.4,True]
print(mylist)

mylist.append("Piha")
print(mylist)

mylist.insert(2,"BR")
print(mylist)

print(len(mylist))
print(mylist[2])
print(mylist[2][0])

print(mylist[2:4])
print(mylist[:2])
print(mylist[:])

mylist[3]=12+4j
print(mylist)

mylist.extend([4, 5])
print(mylist)

mylist[7]=4
print(mylist)
mylist.remove(4)
print(mylist)

mylist.pop(7)
print(mylist)

#mylist.clear() #removes all elements
print(mylist.index(5))

mylist.reverse()
print(mylist)
#mylist.sort()
print(mylist)

new_lst = mylist.copy()
print(new_lst)