#Double list contents

my_list=[1,2,3,4,5,6,7,8,9]

newlist=my_list *2
print(newlist)  # This is not correct way, we have to use loop

templist=[]
for i in my_list:
    temp=i*2
    templist.append(temp)

print(templist)
