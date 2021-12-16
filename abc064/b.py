n = int(input())
num = sorted(list(map(int, input().split())))

print(max(num)-min(num))
