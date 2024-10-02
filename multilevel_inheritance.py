class Demo1:
    def __init__(self):
        self.x=10
    def disp1(self):
        print("present inside the disp1")
class Demo2(Demo1):
    def disp2(self):
        print("present inside the disp2")
class Demo3(Demo2):
    def disp3(self):
        print("present inside the disp3")
d=Demo3()
d.disp3()
d.disp2()
d.disp1()
print(d.x)
