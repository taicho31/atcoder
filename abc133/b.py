import numpy as np
n ,d = map(int, input().split())
ans = 0
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))
    
for i in range(n-1):
    for j in range(i+1,n):
        point1=points[i]
        point2=points[j]
        total = 0
        for k in range(d):
            total += (point1[k]-point2[k])**2
        dist = np.sqrt(total)
        if dist == int(dist):
            ans += 1
                
print(ans)
