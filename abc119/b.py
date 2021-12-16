n = int(input())
ans = 0
for _ in range(n):
    value, kind = input().split()
    if kind == "JPY":
        ans += int(value)
    else:
        ans += float(value) * 380000
print(ans)
