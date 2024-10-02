class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        print(self.name,"is working")
    def play(self):
        print(self.name,"is playing")
e1=Employee('akash',34,40000)
e2=Employee('neha',29,55000)
e1.work()
e1.play()
e2.work()
e2.play()
print(e1.name,e1.age,e1.salary)
print(e2.name,e2.age,e2.salary)
