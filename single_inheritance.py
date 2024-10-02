class Employee:
    def __init__(self):
        self.x=10
    def disp(self):
        print("inside the disp function")

class Employee1(Employee):
    def __init__(self):
        self.y=20
    def disp2(self):
        print("inside the disp2 function")
e=Employee1()
e.disp()
e.disp2()
print(e.y)
