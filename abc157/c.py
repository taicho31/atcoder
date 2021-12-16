# c
n, m =map(int, input().split())
ans = [-1] *n
flg = True
for _ in range(m):
    s, c = map(int, input().split())
    if ans[s-1] == -1:
        ans[s-1] = c
    elif ans[s-1] != c:
        flg = False
    else:
        pass
    
if n > 1 and ans[0]== 0:
    flg = False
    
if flg:
    for i in range(n):
        if ans[i] == -1:
            if n > 1:
                if i == 0:
                    ans[i] = 1
                else:
                    ans[i] = 0
            else:
                ans[i] = 0
    num = ""
    for i in ans:
        num += str(i)
    print(int(num))
else:
    print(-1)
