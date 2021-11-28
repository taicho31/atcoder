##### a
a = int(input())
b = int(input())
h = int(input())

area = (a + b) * h / 2
area = int(area)
print(area)

##### b
s_a = input()
s_b = input()
s_c = input()

next_turn = 'A'

while True:
    if next_turn == 'A':
        if len(s_a) == 0:
            break
        next_turn = s_a[0].upper()    
        s_a = s_a[1:]
    elif next_turn == 'B':
        if len(s_b) == 0:
            break
        next_turn = s_b[0].upper()    
        s_b = s_b[1:]
    else:
        if len(s_c) == 0:
            break
        next_turn = s_c[0].upper()    
        s_c = s_c[1:]

print(next_turn)
