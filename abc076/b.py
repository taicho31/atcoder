n = int(input())
k = int(input())
ans = 1

for _ in range(n):
     ans = min(2*ans, k+ans)

print(ans)
