dict1={'a':1,'b':2}
dict2={'b':3,'c':4}
dict1.update(dict2)
merger_dict={**dict1,**dict2}
print(merger_dict)
merged_dict=dict1|dict2
print(merged_dict)
