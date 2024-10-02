class Employee:
    def work(self):
        print("emplyee-01 is working")
    def work(self,name):
        print("emplyee-02 is working")
    def work(self,name,age):
        print("emplyee-03 is working")
e1=Employee()
#e1.work()
#e1.work('akash')
e1.work('akash',34)
