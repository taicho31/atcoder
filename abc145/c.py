# c 
import itertools
import numpy as np
n = int(input())

seq = [i for i in range(n)]
points = [list(map(int, input().split())) for _ in range(n)]
ptr = list(itertools.combinations(seq, 2))
route_num = len(list(itertools.combinations(seq, n)))

coef =  route_num * (n-1) / len(ptr)

ans = 0
for i in ptr:
    point1 = points[i[0]]
    point2 = points[i[1]]
    
    length = np.sqrt((point1[1] - point2[1])**2 + (point1[0] - point2[0])**2)
    ans += length * coef
    
print(ans / route_num)
