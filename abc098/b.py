n = int(input())
s = input()
ans = 0

for i in range(1, n):
    left = set(s[:i])
    right = set(s[i:])
    length = len(left.intersection(right))
    if ans < length:
        ans = length
    
print(ans)
