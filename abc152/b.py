# b
a, b = input().split()

a_s = str(a * int(b))
b_s = str(b * int(a))

print(min(a_s, b_s))
