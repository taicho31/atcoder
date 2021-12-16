n = int(input())
blue = dict()
for _ in range(n):
    i = input()
    blue[i] = blue.get(i, 0) + 1
    
m = int(input())
for _ in range(m):
    i = input()
    blue[i] = blue.get(i, 0) - 1    

ans = 0
for k in blue.keys():
    if blue[k] > ans:
        ans = blue[k]
        
print(ans)
