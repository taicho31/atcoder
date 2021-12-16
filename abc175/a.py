# a
s = input()

if s.count("R") != 2:
    print(s.count("R"))
else:
    if s.count("RR") == 1:
        print(2)
    else:
        print(1)
