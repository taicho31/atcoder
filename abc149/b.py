# b
a, b, k = map(int, input().split())

if a >= k:
    a -=k
else:
    remain = k -a
    a = 0
    if b < remain:
        b = 0
    else:
        b -= remain
print(a, end=" ")
print(b)
