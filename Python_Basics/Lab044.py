def make_Pizza(*toppings):
    print(toppings)
    print(type(toppings))
    for topin in toppings:
        print(topin)


make_Pizza("Tomato","Onion")
make_Pizza("Tomato","Cheese","Onion","Panner")