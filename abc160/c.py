# c
k, n = map(int, input().split())
houses = list(map(int, input().split()))

diff = [houses[i+1]-houses[i] for i in range(n-1)]
last = houses[-1] - houses[0]
last = min(k-last, last)

diff.append(last)

print(sum(diff)- max(diff))
