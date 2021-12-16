# c 
from collections import Counter
n = int(input())

count = Counter()
for _ in range(n):
    s = input()
    count.update([s])
    
values = list(count.values())
strings = list(count.keys())
maxi = max(values)

ans = []
for i in range(len(strings)):
    if values[i] == maxi:
        ans.append(strings[i])
        
ans = sorted(ans)
for i in ans:
    print(i)
