# c
def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

n = int(input())

while True:
    if is_prime(n):
        break
    n += 1
    
print(n)
