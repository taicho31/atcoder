# b 
a, b, c, d = map(int, input().split())
takahashi_count = c // b if c % b == 0 else c//b + 1
aoki_count = a // d if a % d == 0 else a//d + 1

if takahashi_count <= aoki_count:
    print("Yes")
else:
    print("No")
