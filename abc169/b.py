# b 
n = int(input())
nums = sorted(list(map(int, input().split())))
flg = True
ans = 1
for num in nums:
    ans *= num
    if ans > 10 ** 18:
        flg = False
        break
    if ans == 0:
        break
        
if flg:
    print(ans)
else:
    print(-1)
