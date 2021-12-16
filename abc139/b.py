# b
a, b = map(int, input().split())

if b == 1:
    print(0)
else:
    count = 1
    while True:
        if a * 1 + (a-1) * (count-1)>= b:
            break
        count += 1
    print(count)
