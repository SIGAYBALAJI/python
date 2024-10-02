string=input()
sum1=0
for num in string:
    if ord(num)>=48 and ord(num)<=57:
        sum1=sum1+int(num)
print(str(sum1))
