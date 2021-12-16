n = int(input())
ps = list(map(int, input().split()))
ans = 0

for i in range(1, n-1):
    if (ps[i-1] < ps[i] and ps[i] < ps[i+1]) or (ps[i-1] > ps[i] and ps[i] > ps[i+1]):
        ans += 1
        
print(ans)
