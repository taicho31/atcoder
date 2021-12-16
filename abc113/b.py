n = int(input())
T, A = map(int, input().split())

points = list(map(int, input().split()))

diff = abs(A-(T-points[0]*0.006))
ans = 0

for i in range(1,n):
    if abs(A-(T-points[i]*0.006)) < diff:
        diff = abs(A-(T-points[i]*0.006))
        ans = i
        
print(ans+1)
