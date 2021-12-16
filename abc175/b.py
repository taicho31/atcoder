# b
import itertools

n = int(input())
nums = list(map(int, input().split()))

ptr = itertools.combinations(range(n), 3)
ans = 0

for i in ptr:
    tmp = [nums[i[0]], nums[i[1]], nums[i[2]]]
    if len(set(tmp))==3 and max(tmp) < sum(tmp)-max(tmp):
        ans += 1

print(ans)
