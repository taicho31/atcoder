n, k = map(int, input().split())
s = input()
ans = ""
tmp = s[k-1].lower()
for i in range(n):
    if i == k-1:
        ans += tmp
    else:
        ans += s[i]
        
print(ans)
