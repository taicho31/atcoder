n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

cities =[a,b,c,d,e]

bottleneck = sorted(range(len(cities)), key=lambda x: cities[x])[0]

if n % cities[bottleneck] == 0:
    ans = (n // cities[bottleneck]) + 4
else:
    ans =  (n // cities[bottleneck]) + 5

print(ans)
