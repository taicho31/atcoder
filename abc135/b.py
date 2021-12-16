n = int(input())
nums = list(map(int, input().split()))

sorted_nums = sorted(nums)
count = 0
for i in range(n):
    if nums[i] !=sorted_nums[i]:
        count += 1
        
if count == 2 or count == 0:
    print("YES")
else:
    print("NO")
