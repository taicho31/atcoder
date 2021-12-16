h, w = map(int, input().split())

grids = []
for _ in range(h):
    inp = input()
    if inp.count('.') != w:
        grids.append(inp)
    
remove_index = []
for j in range(w):
    tmp = ""
    for i in range(len(grids)):
        tmp += grids[i][j]
    if tmp.count('.') == len(grids):
        remove_index.append(j)
    
cons_column = [i for i in range(w) if i not in remove_index]
    
for i in range(len(grids)):
    for j in cons_column:
        print(grids[i][j], end="")
    print("")
