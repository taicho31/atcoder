n = int(input())
num = set(map(int, input().split()))

if len(num)==n and sum(num) == int(n * (n+1) / 2):
    print("Yes")
else:
    print("No")
