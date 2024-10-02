nums=[3,4,2,6,7,1,8]
n=len(nums)
min=nums[0]
for i in range(n):
    if nums[i]<min:
        min=nums[i]
        index=i
print(f"min element:{min}",f"index of:{index}")
