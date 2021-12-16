# c
a, b = map(int, input().split())

flg = False
for i in range(1, 1010):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        flg = True
        break
if flg:
    print(i)
else:
    print(-1)
