#using While loop
'''def findfactor(num):
    i=1
    while num!=0:
        if num%i==0:
            print(i)
        i=i+1

res=findfactor(int(input("enter the number")))
print(res)'''
#using For loop
def find_factor(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
res=find_factor(int(input("enter the number ")))

