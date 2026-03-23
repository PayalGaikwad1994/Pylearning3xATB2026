#Lambda + Map

my_list = [1,2,3,4,5,6,7,8,9,10]

def double_item(num):
    return num * 2

double_list= list(map(double_item, my_list))
print(double_list)

double_item_lambda=lambda num:num*2
double_list1= list(map(double_item, my_list))
print(double_list1)

print(list(map(lambda num:num *2,[2,3,5,6]))) #one liner
