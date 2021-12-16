# c
h, n = map(int, input().split())
monsters = sorted(list(map(int, input().split())), reverse=True)

print(sum(monsters[n:]))
