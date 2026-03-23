mylist1 = [1,2,3,4,5,6,7,8,9]

def do_something1(payallist):
    payallist.append('hello')
    payallist[0]=100
    return payallist

mylist1.append("Chima")
l1=do_something1(mylist1)
print(l1)