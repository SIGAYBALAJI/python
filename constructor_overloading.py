class Employee:
    def __init__(self):
        print("inside constructor-01")
    def __init__(self,name):
        print("inside constructor-02")
    def __init__(self,name,age):
        print("inside constructor-03")
e1=Employee('akash',34)
