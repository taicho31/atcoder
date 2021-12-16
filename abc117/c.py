n, m  = map(int, input().split())

coords = sorted(list(map(int, input().split())))
diff = sorted([coords[i]-coords[i-1] for i in range(1, len(coords))])

if n >= m:
    print(0)
else:
    if n !=1:
        print(sum(diff[:-(n-1)]))
    else:
        print(sum(diff))
