# b
k, x = map(int, input().split())
ans = [i for i in range(x-k+1, x+k)]
for i in ans:
    if i == x+k-1:
        print(i)
    else:
        print(i, end= " ")
