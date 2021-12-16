a, b = input().split()
num = int(a+b)
flg = False

for i in range(321):
    if i * i ==num:
        flg = True
        break

if flg:
    print("Yes")
else:
    print("No")
