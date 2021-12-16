s = input().split("/")
s = [int(i) for i in s]

if s[0] <= 2019 and s[1] <= 4 and s[2] <=30:
    print("Heisei")
else:
    print("TBD")
