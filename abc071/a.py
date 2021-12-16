x, a, b = map(int, input().split())
a_dist = abs(x-a)
b_dist = abs(x-b)
if a_dist < b_dist:
    print("A")
else:
    print("B")
