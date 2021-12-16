n = int(input())
nums = []
for _ in range(n):
    tmp = int(input())
    nums.append(tmp)
    
nums = sorted(nums, reverse=True)
ans = nums[0]//2
for i in range(1,n):
    ans += nums[i]
print(ans)
