n,k = map(int, input().split())
remain = k
pairs = [tuple(map(int, input().split())) for i in range(n)]
pairs = sorted(pairs)
    
for i in range(n):
    if remain >= pairs[i][0]:
        remain +=pairs[i][1]
        if i == n-1:
            print(remain)
    else:
        print(remain)
        break
