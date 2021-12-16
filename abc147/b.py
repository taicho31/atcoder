# b
s = input()
length = len(s)
ans = 0

for i in range(length//2):
    if s[i] != s[length-i-1]:
        ans += 1
print(ans)
