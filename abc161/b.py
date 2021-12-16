# b
n, m = map(int, input().split())
nums = list(map(int, input().split()))

count = 0

for i in nums:
    if i >= sum(nums) / (4*m):
        count += 1
        
if count >= m:
    print("Yes")
else:
    print("No")
