n, l = map(int, input().split())
apples = [l-1+i for i in range(1, n+1)]

original_sum = sum(apples)
tmp_sum = sum(apples[1:])
diff = abs(original_sum - tmp_sum)
ans = tmp_sum

for i in range(1,n):
    tmp_sum = tmp_sum - apples[i] + apples[i-1]
    if abs(original_sum - tmp_sum) < diff:
        ans = tmp_sum
        diff = abs(original_sum - tmp_sum)
        
print(ans)
