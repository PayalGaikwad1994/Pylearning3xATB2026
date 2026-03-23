global_a=10

def check_global():
    print(global_a)

check_global()

def outer_function():
    a=10
    def inner_function():
        print(a)

    inner_function()

outer_function()