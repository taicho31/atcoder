n = int(input())
a = list(map(int, input().split()))
x = int(input())

sum_a = sum(a)
remain = x % sum_a
prev_num = x // sum_a

tmp = 0
for index, elem in enumerate(a):
    tmp += elem
    if tmp > remain:
        break
print(prev_num*n+index+1)
