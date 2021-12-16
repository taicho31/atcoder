# b
n = int(input())
flg = False
for i in range(1, 10):
    for j in range(1, 10):
        if i *j == n:
            flg = True
            
if flg:
    print("Yes")
else:
    print("No")
