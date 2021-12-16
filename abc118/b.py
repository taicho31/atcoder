n, m = map(int, input().split())
common = list(map(int, input().split()))[1:]

for _ in range(1, n):
    new = list(map(int, input().split()))[1:]
    common = [i for i in common if i in new]
    
print(len(common))
