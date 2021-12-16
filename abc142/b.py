# b 
n, h = map(int, input().split())
heights = list(map(int, input().split()))

ans = 0
for i in heights:
    if i >=h:
        ans += 1
print(ans)
