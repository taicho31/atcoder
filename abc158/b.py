# b 
n, a, b =map(int, input().split())

time = n // (a+b)
remain = n % (a+b)

if remain < a:
    print(time*a+remain)
else:
    print(time*a+a)
