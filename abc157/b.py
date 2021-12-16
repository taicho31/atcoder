# b 
nums = []
for _ in range(3):
    nums.append(list(map(int, input().split())))
    
n = int(input())
for _ in range(n):
    num = int(input())
    for i in range(3):
        for j in range(3):
            if num == nums[i][j]:
                nums[i][j] = -1

flg = False
for i in range(3):
    if nums[i][0] + nums[i][1] + nums[i][2] == -3:
        flg = True
        
for i in range(3):
    if nums[0][i] + nums[1][i] + nums[2][i] == -3:
        flg = True
    
if (nums[0][0] + nums[1][1] + nums[2][2] == -3) or (nums[0][2] + nums[1][1] + nums[2][0] == -3):
    flg = True 
    
if flg:
    print("Yes")
else:
    print("No")
