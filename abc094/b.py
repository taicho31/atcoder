n, m, x = map(int, input().split())

cost = list(map(int, input().split()))

left = len([i for i in cost if i < x])
right = m - left

print(min(left, right))
