import re

s = open("input.txt").read().strip().splitlines()
i = 0
shapes_raw ={}
queries =[]
sid= None
grid = []

while i< len(s):
    line =s[i].strip()
    i+= 1
    if not line: continue
    if 'x' in line and ':' in line and line.split(':')[0].replace('x','').isdigit():
        queries.append(line)
        continue
    if line.endswith(':') and line[:-1].isdigit():
        if sid is not None:
            shapes_raw[sid]= grid
        sid = int(line[:-1])
        grid =[]
        continue
    if sid is not None:
        grid.append(line)

if sid is not None:
    shapes_raw[sid] = grid

shapes ={}
for k, g in shapes_raw.items():
    pts =set()
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            if ch == '#':
                pts.add((r, c))
    shapes[k] = pts

def norm(v):
    mn_r= min(r for r, c in v)
    mn_c = min(c for r, c in v)
    return tuple(sorted((r -mn_r, c -mn_c) for r, c in v))

def variants(base):
    res= set()
    b = list(base)
    ts =[lambda r,c:(r, c), lambda r,c:(c,-r), lambda r, c:(-r,-c), lambda r, c:(-c, r), lambda r, c:(r,-c),
        lambda r, c:(-c,-r), lambda r, c:(-r, c),lambda r,c:(c, r),]
    for f in ts:
        v =[f(r,c) for r, c in b]
        res.add(norm(v))
    return [list(v) for v in res]

shape_var= {k: variants(v) for k,v in shapes.items()}

def gen_masks(vs, w, h):
    out= []
    for v in vs:
        maxr =max(r for r, c in v)
        maxc= max(c for r,c in v)
        if maxr>= h or maxc >= w: continue
        for r0 in range(h - maxr):
            for c0 in range(w - maxc):
                m = 0
                for r, c in v:
                    idx = (r0 + r) * w + (c0 + c)
                    m|= (1 << idx)
                out.append(m)
    return out

ans=0

for line in queries:
    head, tail=line.split(':')
    w, h =map(int, head.split('x'))
    need =list(map(int, tail.split()))
    area =sum(len(shapes[i]) * need[i] for i in range(len(need)) if need[i] > 0)
    if area>w * h:
        continue
    if area==0:
        ans+= 1
        continue

    groups =[]
    for i, cnt in enumerate(need):
        if cnt > 0:
            groups.append((i, cnt, len(shapes[i])))
    groups.sort(key=lambda x: x[2], reverse=True)

    masks ={}
    ok = True
    for sid, cnt, i in groups:
        m = gen_masks(shape_var[sid], w, h)
        if not m:
            ok = False
            break
        masks[sid] = m
    if not ok:
        continue

    def fit(gi, rc, board, start):
        if gi >= len(groups):
            return True
        sid,cnt,i = groups[gi]
        ms = masks[sid]
        for idx in range(start, len(ms)):
            m = ms[idx]
            if board & m == 0:
                nb =board | m
                if rc> 1:
                    if fit(gi, rc - 1, nb, idx + 1):
                        return True
                else:
                    if fit(gi + 1, groups[gi + 1][1] if gi + 1 < len(groups) else 0, nb, 0):
                        return True
        return False

    sid0, cnt0,i=groups[0]
    if fit(0, cnt0, 0, 0):
        ans += 1

open("output-p1.txt", "w").write(str(ans))
