s = input()
cha = list(set(s))
flg = True
if len(cha) == 2:
    for i in cha:
        if s.count(i) != 2:
            flg = False
            break
else:
    flg = False
    
if flg:
    print("Yes")
else:
    print("No")
