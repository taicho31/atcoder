##### a
n = int(input())
k = int(input())
x = int(input())
y = int(input())

if n>=k:
    print(x*k + y*(n-k))
else:
    print(x*n)

##### b
string = ''.join(sorted(input()))
flg = True
    
if len(string) % 2 ==1:
    flg = False
else:
    for i in range(0, len(string), 2):
        if string[i] != string[i+1]:
            flg = False
            break

if flg:
    print("Yes")
else:
    print("No")

##### c
import itertools 
n ,a = map(int, input().split())
nums = list(map(int, input().split()))

ans = 0

for i in range(1, n+1):
    elements = itertools.combinations(nums, i)
    for j in elements:
        if sum(j) / i ==a:
            ans += 1

print(ans)
