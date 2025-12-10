import re

s = open("input.txt").read().strip().splitlines()
i = 0
res = []

while i < len(s):
    line = s[i].strip()
    i += 1
    if not line:
        continue
    t = line.split('{')[0]
    parts = t.strip().split()
    pat = parts[0][1:-1]
    btns = []
    for p in parts[1:]:
        if p.startswith('('):
            p = p.strip('()')
            btns.append([int(x) for x in p.split(',')] if p else [])
    n = len(pat)
    targ = 0
    for k,c in enumerate(pat):
        if c == '#':
            targ |= 1 << k
    masks = []
    for b in btns:
        m = 0
        for x in b:
            m |= 1 << x
        masks.append(m)
    best = 10**9
    tlen = len(masks)
    for mask in range(1 << tlen):
        cur = 0
        cnt = 0
        for j in range(tlen):
            if mask & (1 << j):
                cur ^= masks[j]
                cnt += 1
                if cnt >= best:
                    break
        if cur == targ and cnt < best:
            best = cnt
    res.append(best)

open("output-p1.txt", "w").write(str(sum(res)))
