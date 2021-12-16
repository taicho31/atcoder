# b
n, k = map(int, input().split())
people = []
for _ in range(k):
    num = int(input())
    tmp = list(map(int, input().split()))
    for i in tmp:
        if i not in people:
            people.append(i)
            
print(n-len(people))
