#exception handler in mutiple method
def alpha():
    try:
        print("connection of alpha established")
        a=10
        b=0
        print(a/b)
        print("connection of alpha ended")
    except:
        print("exception handled")
def beta():
    print("connection of beta established")
    alpha()
    print("connection of beta ended")
def gamma():
    print("connection of gamma established")
    beta()
    print("connection of gamma ended")
gamma()
