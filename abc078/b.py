x, y, z = map(int, input().split())

ans = 1
while True:
    if y * (ans+1) + z * (ans+1+1) > x:
        break
        
    ans +=1
print(ans)
