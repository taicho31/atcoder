string = ''.join(sorted(input()))
flg = True
    
if len(string) % 2 ==1:
    flg = False
else:
    for i in range(0, len(string), 2):
        if string[i] != string[i+1]:
            flg = False
            break

if flg:
    print("Yes")
else:
    print("No")
