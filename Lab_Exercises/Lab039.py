def you_are_allowed_to_enter(name,password):
    if name=="payal":
        if password=="Yes":
            print("You are allowed")
        else:
            print("You are not allowed")

you_are_allowed_to_enter("payal","Yes")

def you_allowed_python_class(name):
    match name:
        case "payal":
            print("You are allowed")
        case "Komal":
            print("You are allowed")
        case _:
            print("You are not allowed")


you_allowed_python_class('Mica')
