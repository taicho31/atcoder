n, k = map(int, input().split())

remain = n % k 
if remain:
    print(1)
else:
    print(0)
