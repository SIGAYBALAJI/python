class Demo:
    def play(self):#inherited method
        print("player is playing")
    def cook(self):
        print("parent is cooking")
class Demo1(Demo):
    def study(self):#specialized method
        print("chlid is studying")
    def cook(self):#overridden method
        print("chlid is cooking")
d1=Demo1()
d1.study()
d1.cook()
d1.play()
