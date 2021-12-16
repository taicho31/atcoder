# b 
n = int(input())
meals = list(map(int, input().split()))
benefit = list(map(int, input().split()))
con = list(map(int, input().split()))

ans = sum(benefit)

for i in range(n-1):
    prev = meals[i]
    after = meals[i+1]
    if after - prev == 1:
        ans += con[prev-1]
    
print(ans)
