# b
s = input()
t = input()
ans = 0
length = len(s)
for i in range(length):
    if s[i] != t[i]:
        ans += 1
print(ans)
