a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
elems = [a, b, c, d, e]

a_diff = 10 - a % 10 if a%10!=0 else 0
b_diff = 10 - b % 10 if b%10!=0 else 0
c_diff = 10 - c % 10 if c%10!=0 else 0
d_diff = 10 - d % 10 if d%10!=0 else 0
e_diff = 10 - e % 10 if e%10!=0 else 0

diffs = [a_diff, b_diff,c_diff,d_diff,e_diff]

order = sorted(range(len(diffs)), key=lambda x: diffs[x]) 
ans = 0

for i in order[:-1]:
    ans += elems[i]
    if diffs[i] !=0:
        ans += diffs[i]
    
ans += elems[order[-1]]

print(ans)
