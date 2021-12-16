# b
def check(s):
    return s == s[::-1]

s = input()
length = len(s)

if check(s) and check(s[:(length-1)//2]) and check(s[(length+1)//2:]):
    print("Yes")
else:
    print("No")
