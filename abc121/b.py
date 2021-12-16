n, m, c = map(int, input().split())
ans = 0
b_s = list(map(int, input().split()))

for _ in range(n):
    tmp = 0
    a_s = list(map(int, input().split()))
    for i in range(m):
        tmp += a_s[i] * b_s[i]
    tmp += c
    if tmp > 0:
        ans += 1
        
print(ans)
