#Set: Collection of unordered unique items

setA={1,2,2,3,4,4,4,4,7,8,9}
print(setA)

listA=["Maya","Maya",True,True,12.5,90,False]
setB=set(listA)
print(setB)

#intersection,differences and uniion with Set

set1={1,2,3,4,4,5,6,7,8,9}
set2={4,5,11,12,13}
print(set1)
print(set2)
print(set.union(set1,set2))
print(set.intersection(set1,set2))
print(set.difference(set1,set2))
print(set1.difference(set2))
print(set1.intersection(set2))

setP={1,2,3,4,4,5,6,7,8,9}
setQ={2,3,4}
setR={61,72,10}
print(setQ.issubset(setP))
print(setR.isdisjoint(setP))
setR.add(90)
print(setR)
setQ.remove(4)
print(setQ)