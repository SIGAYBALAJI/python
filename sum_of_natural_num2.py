def getsumof(num):
    if num==1:
        return 1
    return num+getsumof(num-1)
num=5
print(getsumof(num))
