w, a, b = map(int, input().split())
if b + w <= a:
    print(a - b -w)
elif b >= a + w:
    print(b-a-w)
else:
    print(0)
