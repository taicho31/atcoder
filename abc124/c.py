s = input()
n = len(s)

ans1 = 0
ans2 = 0

pattern1= ""
pattern2= ""
for i in range(n):
    if i %2 == 0:
        pattern1 += "1"
        pattern2 += "0"
    else:
        pattern1 += "0"
        pattern2 += "1"

for i in range(n):
    if pattern1[i] != s[i]:
        ans1 += 1
    
    if pattern2[i] != s[i]:
        ans2 += 1
        
print(min(ans1, ans2))
