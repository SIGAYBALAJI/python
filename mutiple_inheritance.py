class Demo1:
    def __init__(self):
        self.x=10
    def disp1(self):
        print("present inside the disp1")
class Demo2:
    def disp2(self):
        print("present inside the disp2")
class Demo3(Demo1,Demo2):
    def disp3(self):
        print("present inside the disp3")
d3=Demo3()
d3.disp1()
