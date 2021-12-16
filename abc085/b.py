n = int(input())

ans = []
for _ in range(n):
    tmp = int(input())
    if tmp not in ans:
        ans.append(tmp)
print(len(ans))
