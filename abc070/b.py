a, b, c, d = map(int, input().split())

if b < c or d < a:
    print(0)
else:
    lower = max(a, c)
    upper = min(b, d)
    print(upper-lower)
