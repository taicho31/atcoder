n, m = map(int, input().split())

students = [list(map(int, input().split())) for _ in range(n)]
points = [list(map(int, input().split())) for _ in range(m)]
          
for i in range(n):
    dist = 10 **9
    loc = -1
    for j in range(m):
        tmp = abs(students[i][0] - points[j][0]) + abs(students[i][1] - points[j][1])
        if tmp < dist:
            dist = tmp
            loc = j+1
    print(loc)
