# c
n = int(input())
s = input()
count = 1
prev = s[0]
for ele in s[1:]:
    if ele != prev:
        count +=1
    prev=ele
print(count)
