w, h, n = map(int, input().split())

nums = []
x_min = 0
x_max = w
y_min = 0
y_max = h

for _ in range(n):
    x, y, a =  map(int, input().split())
    if a == 1:
        x_min = max(x_min, x)
    elif a == 2:
        x_max = min(x_max, x)
    elif a == 3:
        y_min = max(y_min, y)
    else:
        y_max = min(y_max, y)
    
if x_max <= x_min or y_max <= y_min:
    print(0)
else:
    area = (x_max - x_min) * (y_max - y_min)
    print(area)
