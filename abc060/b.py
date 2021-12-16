a, b, c = map(int, input().split())

num = 1
remain = []
flg = False

while True:
    tmp_num = b * num + c
    tmp_remain = tmp_num % a
    if tmp_remain == 0:
        flg = True
        break
    elif tmp_remain in remain:
        break
    else:
        remain.append(tmp_remain)
    num += 1
        
if flg:
    print("YES")
else:
    print("NO")
