n = int(input())

maxi = n // 4
flg = False

for i in range(maxi+1):
    remain = n - 4 * i
    if remain % 7 == 0:
        flg = True
        break
        
if flg:
    print("Yes")
else:
    print("No")
