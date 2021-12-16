s = input()

if s[0] == 'A' and s[2:-1].count('C')==1:
    
    for i in range(len(s)):
        if s[i] == 'C':
            break
    new_s = ""
    for i in range(1, len(s)):
        if s[i] != 'C':
            new_s += s[i]
            
    if new_s.islower():
        print("AC")
    else:
        print("WA")
else:
    print("WA")
