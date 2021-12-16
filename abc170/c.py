x, n = map(int, input().split())
nums = sorted(list(map(int, input().split())))
diff = sorted([abs(i - x) for i in nums])

for i in range(100):
    if i == 0 and i in diff:
        pass
    elif sum([j==i for j in diff])==2:
        pass
    else:
        break
        
if x - i not in nums:
    print(x-i)
else:
    print(x+i)
