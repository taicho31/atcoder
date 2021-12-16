x, a, b = map(int, input().split())

eat_day = b - a

if eat_day <=0:
    print("delicious")
elif eat_day <= x:
    print("safe")
else:
    print("dangerous")
