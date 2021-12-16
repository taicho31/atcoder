nums = list(map(int, input().split()))
zero = [i for i in range(len(nums)) if nums[i]==0][0]
print(zero+1)
