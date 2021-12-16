x1, y1, x2, y2 = map(int, input().split())

diff_x = x2-x1
diff_y = y2-y1

x3 = x2 - diff_y
y3 = y2 + diff_x

x4 = x1+x3-x2
y4 = y1+y3-y2

ans = [x3, y3, x4, y4]
for i in range(len(ans)):
    if i != 3:
        print(ans[i], end=" ")
    else:
        print(ans[i])
