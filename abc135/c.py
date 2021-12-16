n = int(input())
monsters = list(map(int, input().split()))
capa = list(map(int, input().split()))

real = [0] * (n+1)

real[0] = min(monsters[0], capa[0])
capa[0] -= real[0]

for i in range(1, n):
    inc = min(monsters[i], capa[i-1])
    monsters[i] -= inc
    real[i] += inc
    capa[i-1] -= inc
    
    inc = min(monsters[i], capa[i])
    monsters[i] -= inc
    real[i] += inc
    capa[i] -= inc
    
real[n] = min(monsters[n], capa[n-1])
capa[n-1] -= real[n]
        
print(sum(real))
