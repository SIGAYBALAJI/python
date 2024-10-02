n=int(input())
s=n
l=[]
sum1=0
while(n>0):
    x=n%10
    l.append(x)
    n=n//10
    sum1=sum(l)
if s%sum1==0:
    print("Harshad number")
else:
    print("Not a harshad Number")
    
