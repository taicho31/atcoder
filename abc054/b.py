n, m = map(int, input().split())
a = [input() for _ in range(n)]
b = [input() for _ in range(m)]

flg = False

for i in range(n-m+1):
    for j in range(n-m+1):
        a_tmp = [a[k][j:j+m] for k in range(i, i+m)]
        if a_tmp == b:
            flg = True
            break
            
    if flg:
        break
        
if flg:
    print("Yes")
else:
    print("No")
