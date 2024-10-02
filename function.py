def greeting_function():
    print('welcome to function')
greeting_function()

def greeting_function(name):
    print('welcome '+name)
greeting_function('tom')  

def greeting_function(name,age):
    print('your name is '+ name +' and age is '+str(age))
greeting_function('tom',21)  

def greeting_function(*names):
    print('welcome '+names[1])
greeting_function('tom','john','timy')    

def greeting_function(name,age):
    print('welcome '+name+' your age is '+str(age))
name=input('enter your name:')
age=input('enter your age:')
greeting_function(name,age)    
