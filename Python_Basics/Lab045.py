d={"Name":"Payal"}
print(d)
print(type(d))

def make_pizza(*toppings,base):
    print(toppings,base)

# make_pizza("Tomato","Cheese","Paprika")  -----TypeError: make_pizza() missing 1 required keyword-only argument: 'base'
make_pizza("Tomato","Cheese","Paprika",base="Thin Crust")