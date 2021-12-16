# c
n = int(input())
nums = list(map(int, input().split()))

count = 0
tmp = nums[0]
ans = count

for i in nums[1:]:
    if i <= tmp:
        count +=1
    else:
        count = 0
    tmp = i
    if ans < count:
        ans = count
    
print(ans)
