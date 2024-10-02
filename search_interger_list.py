nums=[0,1,2,4,12]
search=4
n=len(nums)
for i in range(n):
    if nums[i]==search:
        print(search,"at index of",i)
        break
else:
    print(search,"not found in list")
