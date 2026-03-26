#Dictionary: Unordered collection of Key value pair

mydict={
    "a":1,
    "b":2,
    "c":3
}

new_dict=dict(name="payal",age=31)
print(mydict)
print(new_dict)
print(mydict.keys())
print(mydict.values())
print(mydict.items())
print(mydict["a"])
print(mydict["b"])
print(mydict["c"])
mydict["c"]=5
print(mydict)
print(mydict.keys())
print(mydict.values())
print(mydict.get("a"))
