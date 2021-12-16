a = input()
b = input()
flg = False
count = 0

while True:
    if a == b:
        flg = True
        break
        
    if count == len(a):
        break
    
    b = b[-1] + b[:-1]
    count +=1
    
if flg:
    print("Yes")
else:
    print("No")
