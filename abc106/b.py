import numpy as np 
nums = []
for n in range(1, 201, 2):
    count = 0
    for i in range(1, int(np.sqrt(n))+1):
        if n % i == 0:
            count += 1    
    if count * 2 == 8:
        nums.append(n)
        
ans = 0
n = int(input())
for i in nums:
    if i <= n:
        ans += 1
print(ans)
