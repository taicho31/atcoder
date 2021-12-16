a, b, k = map(int, input().split())

div_a = []
for i in range(1, a+1):
    if a % i == 0:
        div_a.append(i)
        
common = []
for i in div_a:
    if b % i == 0:
        common.append(i)
common = sorted(common, reverse=True)
    
print(common[k-1])
