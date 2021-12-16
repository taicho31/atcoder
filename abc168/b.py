# b
k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    ans = s[:k] +"..."
    print(ans)
