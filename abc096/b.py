a, b, c = map(int, input().split())
k = int(input())

total = a + b + c
total -= max(a, b, c)
maxi = max(a, b, c)

for i in range(k):
    maxi *= 2
    
total += maxi
print(total)
