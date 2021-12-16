x = int(input())
flg = False
ans = 0

for b in range(1, 1001):
    for p in range(2, 10):
        if b ** p <=x and ans < b ** p:
            ans = b ** p
            
print(ans)
