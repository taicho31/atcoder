s = input()

if len(s) % 2 == 0:
    for i in range(2, len(s),2):
        tmp = s[:-i]
        if tmp[:len(tmp)//2]== tmp[len(tmp)//2:]:
            break
else:
    for i in range(1, len(s), 2):
        tmp = s[:-i]
        if tmp[:len(tmp)//2]== tmp[len(tmp)//2:]:
            break
            
print(len(tmp))
