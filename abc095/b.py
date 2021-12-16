n, x = map(int, input().split())

donuts = []
for _ in range(n):
    donuts.append(int(input()))
    
x -= sum(donuts)

print(n + x // min(donuts))
