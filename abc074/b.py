n = int(input())
k = int(input())
pos = map(int, input().split())
ans = 0
for ele in pos:
    ans += 2 * min(abs(ele-0), abs(ele-k))
    
print(ans)
