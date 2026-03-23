#function scope

def check_scope():
    a=10
    print(a)

check_scope(a) # a is local to the function, NameError: name 'a' is not defined