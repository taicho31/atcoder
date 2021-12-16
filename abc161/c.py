# c
n, k = map(int, input().split())

remain = n % k

print(min(remain, abs(k-remain)))
