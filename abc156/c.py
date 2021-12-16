# c
n = int(input())
nums = list(map(int, input().split()))

ans = 10 ** 10
for i in range(101):
    tmp = 0
    for j in nums:
        tmp += (i-j)**2
    if tmp < ans:
        ans = tmp
print(ans)
