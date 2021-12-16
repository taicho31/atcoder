# b 
n = int(input())
nums = list(map(int, input().split()))
flg = True

for i in range(n):
    if nums[i] % 2 == 0:
        if nums[i] % 3 != 0 and nums[i] % 5 != 0:
            flg = False
            
if flg:
    print("APPROVED")
else:
    print("DENIED")
