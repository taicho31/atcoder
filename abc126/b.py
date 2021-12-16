s = input()

former = int(s[:2])
latter= int(s[2:])

if former == 0 or former > 12:
    if latter == 0 or latter > 12:
        print("NA")
    else:
        print("YYMM")
else:
    if latter == 0 or latter > 12:
        print("MMYY")
    else:
        print("AMBIGUOUS")
