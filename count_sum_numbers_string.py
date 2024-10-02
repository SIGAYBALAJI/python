string="Daya123Ben456"
sum1=0
for i in string:
    if ord(i)>=48 and ord(i)<=57:
        sum1+=int(i)
print("sum is: "+str(sum1))
