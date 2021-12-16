# c
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

a, b = map(int, input().split()) 

ans = lcm(a, b)

print(ans)
