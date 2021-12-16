n, a, b = map(int, input().split())
ans = 0
for i in range(1, n+1):
    tmp_i = str(i)
    rank = 0
    for j in tmp_i:
        rank += int(j)
    if rank >=a and rank <= b:
         ans += i
            
print(ans)
