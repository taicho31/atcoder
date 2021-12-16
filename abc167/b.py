# b 
a, b, c, k = map(int, input().split())

if a >=k:
    print(k)
elif a + b >= k:
    print(a)
else:
    diff = k - (a+b)
    print(a - diff)
