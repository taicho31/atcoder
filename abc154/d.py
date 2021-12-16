# d
n, k = map(int, input().split())
nums = list(map(int, input().split()))

tmp = 0
for i in range(k):
    tmp += (nums[i] + 1) / 2
ans = tmp
    
for i in range(1, n-k+1):
    tmp += (nums[i+k-1]/2) - (nums[i-1]/2)
    if tmp > ans:
        ans = tmp
    
print(ans)
