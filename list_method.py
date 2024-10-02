list1=[5,3,2,4,1]
list2=['banana','apple','orange','mango']
#combined the lists
#list1.extend(list2)
print(list1)
#append value to list
list2.append('cherry')
print(list2)
print(len(list2))
#insert values in between list
list2.insert(1,'cherry')
print(list2)
#remove particular value
#list2.remove('cherry')
#print(list2)
#clear the all values in the list

#index values of particular value

print(list2.index('apple'))
#count the number values in a list
print(list2.count('cherry'))
list1.sort()
print(list1)
#reverse the list items
list2.reverse()
print(list2)
list3=list2.copy()
print(list3)
#remove the last value in the list
list2.pop()
print(list2)
#delete the list items
del list2[0]
print(list2)