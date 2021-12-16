n = int(input())
nums =list(map(int, input().split()))

while True:
    mini = min([i for i in nums if i != 0]) 
    ind = [i for i in range(len(nums)) if nums[i] == mini][0] 
    nums = [nums[i] % mini  if i != ind else nums[i] for i in range(len(nums))]
    if sum([ele == 0 for ele in nums]) == n-1:
        break
        
print(max(nums))
