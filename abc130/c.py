w, h, x, y = map(int, input().split())

maxi = w * h / 2
print(maxi, end=" ")
if x == w/2 and y == h /2:
    print(1)
else:
    print(0)
