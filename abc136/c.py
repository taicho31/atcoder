n = int(input())
h = list(map(int, input().split()))
flg = True
for i in range(n-2,-1,-1):
    if h[i] - h[i+1] >= 2:
        flg = False
        break
    elif h[i] - h[i+1] ==1:
        h[i]-=1
    else:
        pass
    
if flg:
    print("Yes")
else:
    print("No")
