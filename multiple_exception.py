def div():
    try:
        a=10
        b='kk'
        print(a/b)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except NameError:
        print("NameError")
    except TypeError:
        print("TypeError")
    except:
        print("some error occured")
div()
