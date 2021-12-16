n = int(input())
num = sorted(list(map(int, input().split())))

large_rate = sum([1if i >=3200 else 0 for i in num])

group = [0] * 8
for i in num:
    if 1 <= i <=399:
        group[0] = 1
    elif 400 <= i <=799:
        group[1] = 1
    elif 800 <= i <=1199:
        group[2] = 1
    elif 1200 <= i <=1599:
        group[3] = 1
    elif 1600 <= i <=1999:
        group[4] = 1
    elif 2000 <= i <=2399:
        group[5] = 1
    elif 2400 <= i <=2799:
        group[6] = 1
    elif 2800 <= i <=3199:
        group[7] = 1
    else:
        pass
    
if sum(group) == 0:
    print(1, large_rate)
else:
    print(sum(group), sum(group)+large_rate)
