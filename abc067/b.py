n, k = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)

print(sum(num[:k]))
