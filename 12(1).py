nums=[2,3,5,7]
for i in range(8,1000):
    flag=True
    for b in range(len(nums)):
        if i%nums[b] == 0:
            flag=False
    if flag:
        nums.append(i)
print(nums)
for n in range(30):
    for i in range(len(nums)):
        if 4*n + 117 ==nums[i]:
            print(n)
