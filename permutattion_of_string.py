import itertools
str="abc"
lis=[]
for i in itertools.permutations(str):
    lis.append(i)
    print(i)
