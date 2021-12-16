n = int(input())
ps = sorted(list(map(int, input().split())))

print(ps[n//2] - ps[n//2-1])
