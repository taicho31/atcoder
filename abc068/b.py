n = int(input())
num = [2 ** i for i in range(7)]

for i in num:
    if n >= i:
        ans = i
    else:
        break
        
print(ans)
