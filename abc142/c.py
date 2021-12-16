# c
n = int(input())
nums = list(map(int, input().split()))

sort = sorted(range(n), key=lambda x: nums[x])

for i in range(n):
    if i == n-1:
        print(sort[i]+1)
    else:
        print(sort[i]+1, end=" ")
