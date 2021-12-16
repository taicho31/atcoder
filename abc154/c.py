# c
n = int(input())
nums = sorted(list(map(int, input().split())))

distinct_len = len(set(nums))

if n == distinct_len:
    print("YES")
else:
    print("NO")
