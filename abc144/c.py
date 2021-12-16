# c
def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    return sorted(table)

n = int(input())
div = divisor(n)

if len(div) % 2 != 0:
    place = div[len(div)//2]
    print((place-1)*2)
else:
    place1 = div[len(div)//2-1]
    place2 = div[len(div)//2]
    print(place1 + place2 - 2)
