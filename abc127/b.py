r, d, x2000 = map(int, input().split())

prev= x2000
for _ in range(10):
    x_plus1 = r * prev - d
    print(x_plus1)
    prev = x_plus1
