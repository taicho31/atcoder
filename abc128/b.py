n = int(input())
elems = []
for _ in range(n):
    s, p = input().split()
    elems.append([s,-int(p)])
    
ans = sorted(range(n), key = lambda x: elems[x])

for i in ans:
    print(i+1)
