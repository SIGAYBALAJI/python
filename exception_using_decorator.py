def mydiv(func):
    def wrapper(a,b):
        if b==0:
            print("cannot divide by zero")
        else:
            func(a,b)
    return wrapper


@mydiv
def div(a,b):
    print(a/b)
div(10,5)
