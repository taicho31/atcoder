n, t = map(int, input().split())
ans = 10 **9
for _ in range(n):
    a, b = map(int, input().split())
    if b <= t and a < ans:
        ans = a
    
if ans == 10 ** 9:
    print("TLE")
else:
    print(ans)
