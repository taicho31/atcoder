s = input()
k = int(input())

count1 = 0
for i in s:
    if i == '1':
        count1 +=1
    else:
        break
        
if count1 >= k:
    print(1)
else:
    print(int(i))
