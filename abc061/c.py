n, k = map(int, input().split())
nums = []
total = 0
for _ in range(n):
    num, times = map(int, input().split())
    nums.append([num, times])
    
ans = -1
nums = sorted(nums)
for i in range(n):
    total += nums[i][1]
    if k <= total:
        ans = nums[i][0]
        break

print(ans)
