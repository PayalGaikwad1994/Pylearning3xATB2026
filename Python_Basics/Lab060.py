cities=("Mumbai","Pune","Chennai","Nagar","nashik","Kolhapur")
print(cities)
print("Mumbai" in cities)
print("Delhi" in cities)

#cities.append() #tuple is immutable
new_cities=cities + ("Delhi","Nepal")
print(new_cities)