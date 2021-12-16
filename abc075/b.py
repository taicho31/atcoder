h, w = map(int, input().split())
moji = ['-'*(w+2)]

for _ in range(h):
    tmp = input()
    moji.append('-'+tmp+'-')
moji.append('-'*(w+2))

ans = []

for i in range(1, h+1):
    ans_row = ""
    for j in range(1, w+1):
        if moji[i][j] == "#":
            ans_row += moji[i][j]
        else:
            tmp = moji[i-1][j-1]+moji[i-1][j]+moji[i-1][j+1]+moji[i][j-1]+moji[i][j+1]+moji[i+1][j-1]+moji[i+1][j]+moji[i+1][j+1]
            ans_row += str(tmp.count('#'))
        
    ans.append(ans_row)
    
for i in ans:
    print(i)
        
