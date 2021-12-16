n = int(input())
h = list(map(int, input().split()))

def split(l):
    ret = []
    tmp = []
    for n in l:
        if n == 0:
            ret.append(tmp)
            tmp = []
        else:
            tmp.append(n)
    if tmp:
        ret.append(tmp)
    return ret

def count(l):
    if not l or all([n==0 for n in l]):
        return 0
    c = 0
    splitted = split(l)
    for _l in splitted:
        if not _l:
            continue
        n_min = min(_l)
        _l = [n-n_min for n in _l]
        c += n_min
        c += count(_l)
    return c

print(count(h))
