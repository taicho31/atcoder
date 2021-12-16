n = int(input())
s_n = str(n)

sum_n = 0
for i in s_n:
    sum_n += int(i)
    
if n % sum_n ==0:
    print("Yes")
else:
    print("No")
