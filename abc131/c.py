def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd (a, b)

a, b, c, d = map(int, input().split())

lcm_cd = lcm(c,d)

b_div = b // d +  b // c - b // lcm_cd
a_div = (a-1)// d +  (a-1) // c - (a-1) // lcm_cd

print((b - b_div) - ((a-1) - a_div))
