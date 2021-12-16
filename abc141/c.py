# c
n, k, q = map(int, input().split())
score = [0] * n

for _ in range(q):
    correct = int(input())
    score[correct-1]+=1
        
for i in range(n):
    tmp = score[i]
    score[i] -= (q-tmp)
    score[i] -= tmp
    score[i] += k
    if score[i] <=0:
        print("No")
    else:
        print("Yes")
