class Demo:
    def __init__(self):
        self.x=20
class Demo1(Demo):
    def __init__(self):
       
        self.x=40
        super().__init__()
d1=Demo1()
print(d1.x)
