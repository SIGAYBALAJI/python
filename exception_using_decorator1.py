def mydiv(func):
    def wrapper(name):
        if name=='hi':
            print("cannot process")
        else:
            func(name)
    return wrapper


@mydiv
def str_check(name):
    print(name)
str_check("hi")
