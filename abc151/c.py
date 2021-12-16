# c
n, m = map(int, input().split())
ac = [0] * n
wa = [0] * n

for _ in range(m):
    q, result = input().split()
    q = int(q)
    if result == "AC" and ac[q-1] == 0:
        ac[q-1] += 1
    if result == "WA" and ac[q-1] == 0:
        wa[q-1] += 1
        
wa_total = 0
for i in range(n):
    wa_total += ac[i]  * wa[i]
        
ac_total = sum(ac)

print(ac_total, end=" ")
print(wa_total)
