n, x = map(int, input().split())
l = list(map(int, input().split()))
prev= 0
ans = 1

for i in range(n):
    prev += l[i]
    if prev <= x:
        ans += 1
    else:
        break
    
print(ans)
