l, r = map(int, input().split())
length = min(r - l, 2018)
left = l % 2019 
elems = [left]
for i in range(length):
    cand = (left + i +1) % 2019
    elems.append(cand)
        
ans = 2020

for i in range(len(elems)-1):
    for j in range(i+1, len(elems)):
        tmp = (elems[i] * elems[j]) % 2019
        if ans > tmp:
            ans = tmp
print(ans)
