#b
n = int(input())
nums= list(map(int, input().split()))
ans = 0
for num in nums:
    ans += 1/num
    
print(1/ans)
