a, b, k = map(int, input().split())
ans = []
for i in range(k):
    if a + i <=b:
        ans.append(a+i)
    
for i in range(k-1,-1,-1):
    if b-i not in ans and b-i >=a:
        ans.append(b-i)
        
for i in ans:
    print(i)
