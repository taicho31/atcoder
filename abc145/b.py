# b
n = int(input())
s = input()

if n % 2 != 0:
    print("No")
else:
    flg = True
    for i in range(n//2):
        if s[i] != s[i+n//2]:
            flg = False
    if flg:
        print("Yes")
    else:
        print("No")
