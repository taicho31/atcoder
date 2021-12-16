# b
n = int(input())
s = input()
ans = ""
for ele in s:
    tmp = ord(ele)
    new_num = tmp+n
    if new_num > ord('Z'):
        new_num -= 26
    ans += chr(new_num)
    
print(ans)
