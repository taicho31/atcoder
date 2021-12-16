# a 
n = int(input())

remain = n % 1000

if remain:
    print(1000-remain)
else:
    print(0)
