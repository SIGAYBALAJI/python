s=input("enter the string:")
dsum=0
for i in s:
    if i.isdigit():
        dsum=dsum+int(i)
print(dsum)
