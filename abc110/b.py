n, m, x, y = map(int, input().split())

xs = max(list(map(int, input().split())))
ys = min(list(map(int, input().split())))

flg = False

for i in range(x+1, y+1):
    if i > xs and i <= ys:
        flg = True
        break
        
if flg:
    print("No War")
else:
    print("War")
