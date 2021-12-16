n = input()

org_x = int(n)
fx = 0
for i in n:
    fx +=int(i)
    
if org_x % fx == 0:
    print("Yes")
else:
    print("No")
