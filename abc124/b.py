n = int(input())
elems = list(map(int, input().split()))

ans = 1
maxi = elems[0]
for i in elems[1:]:
    if i >= maxi:
        ans +=1
        maxi = i
print(ans)
