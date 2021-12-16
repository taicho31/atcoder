n = int(input())
d, ans = map(int, input().split())

for _ in range(n):
    i = int(input())
    if d % i ==0:
        ans += d // i 
    else:
        ans += d // i + 1
    
print(ans)
