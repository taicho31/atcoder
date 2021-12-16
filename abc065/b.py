n = int(input())
a = [int(input()) for _ in range(n)]
order = [-1] * n
order[0] = 0
flg = False
next_button = 1

for i in range(n):
    next_button = a[next_button-1]
    if next_button == 2:
         break
    elif order[next_button-1] != -1:
        flg = True
        break
    else:
        order[next_button-1]= i+1
    
if flg:
    print(-1)
else:
    print(i+1)
