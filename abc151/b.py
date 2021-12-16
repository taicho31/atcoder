# b
n,k,m = map(int, input().split())
nums = list(map(int, input().split()))

req = n * m - sum(nums)

if req > k:
    print(-1)
elif req > 0:
    print(req)
else:
    print(0)
