n = int(input())
s = input()

num = 0
maxi = 0

for i in s:
    if i == "I":
        num +=1
    else:
        num -= 1
    if maxi < num:
        maxi = num
        
print(maxi)
