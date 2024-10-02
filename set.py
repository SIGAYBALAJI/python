#Additional operations:
set1={10,40,30,20,70}
print(set1)#{20, 70, 40, 10, 30}
print(len(set1))

#pop():it  will remove first element from  the result/output set.
set1.pop()
print(set1)#{70, 40, 10, 30}
set1.pop()
print(set1)#{40, 10, 30}

#popitem():there is no popitem in set
#set1.popitem()#AttributeError: 'set' object has no attribute 'popitem'
 #update():Add elements from one set to another set.
s1={1,2,3}
s2={4,5,6}
print(s1.update(s2))#None
print(s1)#{1, 2, 3, 4, 5, 6}
