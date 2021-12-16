s = input()
ans = 0
tmp = 0
for i in range(len(s)):
    if s[i] in ['A', 'C', 'G', 'T']:
        tmp += 1
    else:
        if ans < tmp:
            ans = tmp
        tmp = 0
        
if ans < tmp:
    ans = tmp 

print(ans)
