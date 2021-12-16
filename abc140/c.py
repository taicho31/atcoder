# c
n = int(input())
nums = list(map(int,input().split()))

ans = 0
for i in range(n):
    if i == 0:
        ans += nums[0]
    elif i == n-1:
        ans += nums[-1]
    else:
        ans += min(nums[i-1], nums[i])
print(ans)
