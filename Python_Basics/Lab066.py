mydict={"a":1,"b":2,"c":3,"d":4,"e":5,"a":98}
print(mydict)
print(len(mydict))
print(list(mydict.keys()))
print(list(mydict.values()))

for i in list(mydict.keys()):
    print(i)
    print(mydict[i])

for i in list(mydict.values()):
    print(i)

for k,v in mydict.items():
    print(k,v)