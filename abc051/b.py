k, s = map(int, input().split())
ans = 0

mini = min(k, s)

for a in range(mini+1):
    for b in range(mini+1):
            if s - a - b<=k and s- a-b>=0:
                ans += 1
print(ans)
