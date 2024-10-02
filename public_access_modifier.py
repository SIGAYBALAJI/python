class Employee:
    def __init__(self):
        self.x=10
    def disp(self):
        print(self.x)
e1=Employee()
e1.disp()
print(e1.x)
class Employee1:
    def disp1(self):
        #print(self.x)
        print(e1.x)
e2=Employee1()
e2.disp1()
class Employee2(Employee):
    def disp2(self):
        print(self.x)
        print(e1.x)
        print(e3.x)
e3=Employee2()
e3.disp2()
