#printing object reference
class Demo:
    def __init__(self):
        self.name='neha'

    def disp(self):
        print("inside the disp")
    def __str__(self):
        return self.name

d=Demo()
print(d)
