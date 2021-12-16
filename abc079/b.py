bef1 = 2
bef2 = 1

n = int(input())

if n == 1:
    print(bef2)
else:
    for i in range(2, n+1):
        ans = bef1 + bef2
        bef1 = bef2
        bef2 = ans
    print(ans)
