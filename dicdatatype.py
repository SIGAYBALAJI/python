#Operation on dictionaries:
d1={'name':'akash','age':30,'status':'pass'}
print(d1)#{'name': 'akash', 'age': 30, 'status': 'pass'}

#Duplicate key:value pairs are not allowed.
#Duplicate values are allowed for different keys.
#Duplicate  keys are not allowed

#updating values of the given dict:
d1['age']=31
print(d1)#{'name': 'akash', 'age': 31, 'status': 'pass'}

#Adding key:value pairs from one dict to another dict:
d2={'name1':'rekha','age1':27,'status1':'fail'}
print(d2)#{'name': 'rekha', 'age': 27, 'status': 'fail'}
d1.update(d2)
print(d1)#{'name': 'akash', 'age': 31, 'status': 'pass', 'name1': 'rekha', 'age1': 27, 'status1': 'fail'}
print(d2)#{'name': 'rekha', 'age': 27, 'status': 'fail'}

#pop()-used to remove key:value pair of given key as parameter for pop():
#d2.pop()#TypeError: pop expected at least 1 argument, got 0
#d2.pop('age1')<--------->del d2['age1']
#print(d2)#{'name1': 'rekha', 'status1': 'fail'}
#d2.clear()
#print(d2)#{}
#del d2
#print(d2)
d2.popitem()#remove last item of dict
print(d2)#{'name1': 'rekha', 'age1': 27}

