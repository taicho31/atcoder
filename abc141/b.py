# b
s = input()
flg = True

for i in range(len(s)):
    if (i+1) %2 == 0:
        if s[i] not in ['L', 'U', 'D']:
            flg = False
            break
    if (i+1) % 2 != 0:
        if s[i] not in ['R', 'U', 'D']:
            flg = False
            break
            
if flg:
    print("Yes")
else:
    print("No")
