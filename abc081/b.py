n = int(input())
nums = list(map(int, input().split()))
ans = 0

while True:
    remain = [num % 2 for num in nums]
    if sum(remain) == 0:
        ans += 1
        nums = [num //2 for num in nums]
    else:
        break
        
print(ans)
