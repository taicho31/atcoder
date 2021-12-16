n, m = map(int, input().split())
l_ans, r_ans = map(int, input().split())

for _ in range(m-1):
    l, r = map(int, input().split())
    if l_ans < l:
        l_ans = l
    if r_ans > r:
        r_ans = r
    
if r_ans >= l_ans:
    print(r_ans - l_ans + 1)
else:
    print(0)
