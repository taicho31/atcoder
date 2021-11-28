##### a
a, b, c = map(int, input().split())
if [a,b,c] in [[5,7,5], [7,5,5], [5,5,7]]:
    print("YES")
else:
    print("NO")

##### b
n, l = map(int, input().split())

strings = []
for _ in range(n):
    tmp = input()
    strings.append(tmp)
    
strings = sorted(strings)

print(''.join(strings))

##### c
n, k = map(int, input().split())
dislikes = list(input().split())
answer = n

while True:
    contain = False
    for s in str(answer):
        if s in dislikes:
            contain = True
            break
            
    if contain:
        answer += 1
    else:
        break
print(answer)
