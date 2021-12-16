a, b, c = map(int, input().split())

flg = 0
for i in range(a, b+1):
    if i % c ==0:
        flg = 1
        ans = i
        break
if flg:
    print(ans)
else:
    print(-1)
