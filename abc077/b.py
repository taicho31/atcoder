n = int(input())

for i in range(32000):
    if i**2 <=n:
        ans = i ** 2
    else:
        break

print(ans)
