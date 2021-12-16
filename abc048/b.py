a, b, c = map(int, input().split())
maxi = b // c
maxi += 1
mini = (a-1) // c
mini += 1
print(maxi-mini)
