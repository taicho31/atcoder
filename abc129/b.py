n = int(input())
weights = list(map(int, input().split()))
left = sum(weights[:1])
right = sum(weights[1:])
diff = abs(left-right)

for i in range(1,n):
    ele = weights[i]
    left += ele
    right -= ele
    if diff > abs(left-right):
        diff = abs(left-right)
        
print(diff)
