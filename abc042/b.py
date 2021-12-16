n, l = map(int, input().split())

strings = []
for _ in range(n):
    tmp = input()
    strings.append(tmp)
    
strings = sorted(strings)

print(''.join(strings))
