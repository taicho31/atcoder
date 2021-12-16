n = int(input())

prevs = []
flg = True
prev = input()
prevs.append(prev)

for _ in range(1, n):
    s = input()
    if s in prevs or prev[-1] != s[0]:
        flg = False
    prevs.append(s)
    prev = s
    
if flg:
    print("Yes")
else:
    print("No")
