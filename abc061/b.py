n, m = map(int, input().split())
cities = []

for _ in range(m):
    c1, c2 = map(int, input().split())
    cities.append(c1)
    cities.append(c2)
    
cities = sorted(cities)

for i in range(n):
    ans = len([j for j in cities if j == i+1])
    print(ans)
