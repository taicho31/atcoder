n, x = map(int, input().split())
s = input()

for ele in s:
    if ele == 'x':
        if x != 0:
            x -=1
    else:
        x +=1
    
print(x)
