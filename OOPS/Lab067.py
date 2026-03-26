mydict={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5
}
print(mydict)

for k,v in mydict.items():
    if k=="b":
        print("Key with b is found")

op="b" in mydict.keys()
print(op)