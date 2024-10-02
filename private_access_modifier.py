class Employee:
    def __init__(self):
        self.__x=10
    def disp(self):
        print(self.__x)
e=Employee()
e.disp()
print(e._Employee__x)
class Employee1:
    def disp1(self):
         print(e._Employee__x)
         print(self._Employee__x)
         print(e1._Employee__x)
e1=Employee1()
e1.disp1()
    



