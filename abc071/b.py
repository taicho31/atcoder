s = list(sorted(set(sorted(input()))))
org = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
org = org.split()
flg = False
for i in org:
    if i not in s:
        flg = True
        break
if flg:
    print(i)
else:
    print("None")
