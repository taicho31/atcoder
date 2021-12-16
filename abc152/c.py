# c
n = int(input())
nums = list(map(int, input().split()))

ans = 1
mini = nums[0]

for i in range(1, n):
    if nums[i] <=mini:
        ans += 1
        mini = nums[i]
print(ans)
