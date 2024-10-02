class Demo1:
    def __init__(self):
        self.x=10
    def disp1(self):
        print("present inside the disp1")
class Demo2(Demo1):
    def disp2(self):
        print("present inside the disp2")
class Demo3(Demo1):
    def disp3(self):
        print("present inside the disp3")
class Demo4(Demo1):
    def disp4(self):
        print("present inside the disp4")
d=Demo4()
d.disp4()
d.disp1()
d1=Demo2()
d1.disp2()
d1.disp1()

