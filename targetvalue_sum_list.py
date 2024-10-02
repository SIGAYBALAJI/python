num=[2,7,11,5]
target=9
n=len(num)
for i in range(n):
    for j in range(i+1,n):
        if num[i]+num[j]==target:
            print([num[i],num[j]])
