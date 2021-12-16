n = int(input())
t = list(map(int, input().split()))
m = int(input())

sum_time = sum(t)
for _ in range(m):
    pos, new_time = map(int, input().split())
    print(sum_time - t[pos-1] +new_time)
