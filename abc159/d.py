# d
from collections import Counter

n = int(input())
nums = list(map(int, input().split()))

count = Counter()
count.update(nums)

ans = 0
for i in count.values():
    ans += i * (i-1)//2
    
for i in nums:
    tmp = count[i]
    if tmp == 1:
        print(ans)
    else:
        print(ans - (tmp-1))
