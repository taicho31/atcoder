s = input()
diff = abs(753-int(s[:3]))
for i in range(1, len(s)-2):
    tmp = int(s[i:i+3])
    if diff > abs(753-tmp):
        diff = abs(753-tmp)
print(diff)
