n, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))

print(sum(nums[:k]))
