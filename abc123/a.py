a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())

elems = [a,b,c,d,e]
flg = True

for i in elems:
    for j in elems:
        if abs(i-j) > k:
            flg = False
            
if flg:
    print("Yay!")
else:
    print(":(")
