n = int(input())

vs = list(map(int, input().split()))
cs = list(map(int, input().split()))
ans = 0

for i in range(n):
    if vs[i] - cs[i] > 0:
        ans += vs[i] - cs[i]
        
print(ans)
