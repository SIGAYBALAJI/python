class Employee:
    def __init__(self):
        self._x=10
    def disp(self):
        print(self._x)
e1=Employee()
e1.disp()
print(e1._x)
class Employee1:
    def disp1(self):
        #print(self._x)
        print(e1._x)
e2=Employee1()
e2.disp1()
class Employee2(Employee):
    def disp2(self):
        print(self._x)
        print(e1._x)
        print(e3._x)
e3=Employee2()
e3.disp2()
