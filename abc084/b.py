a, b = map(int, input().split())
s = input()
flg = True
for i in range(len(s)):
    if i +1== a + 1:
        if s[i] != '-':
            flg = False
            break
    else:
        if s[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            flg = False
            break

if flg:
    print("Yes")
else:
    print("No")
