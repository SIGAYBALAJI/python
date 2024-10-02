num=14
p=num
sum1=0
for i in range(num):
    digit=num%10
    sum1+=digit
    num//=10
if p%sum1==0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")