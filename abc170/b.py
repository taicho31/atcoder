x, y = map(int, input().split())
try_num = y//2
flg = False
for i in range(try_num+1):
    if 2*i + 4*(x-i) == y:
        flg = True
        break

if flg:
    print("Yes")
else:
    print("No")
