class Demo:
    def __init__(self):
        self.x=10
        self.y=20
    def __add__(self,other):
        return self.x+other.y
d1=Demo()
d2=Demo()
print(d1+d2)
