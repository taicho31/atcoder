# c
from collections import Counter
n = int(input())

count = Counter()
for _ in range(n):
    s = ''.join(sorted(input()))
    count.update([s])
     
ans = 0
for i in count.values():
    ans += i * (i-1) // 2
print(ans)
