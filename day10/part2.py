import re
import numpy as np
from scipy.optimize import milp, linearconstraint, bounds

s=open("input.txt").read().strip().splitlines()
i =0
res= []

while i <len(s):
    line =s[i].strip()
    i += 1
    if not line:
        continue
    m= re.search(r'\{([\d,]+)\}', line)
    if not m:
        continue
    b =np.array([int(x) for x in m.group(1).split(',')])
    n =len(b)
    btns= re.findall(r'\(([\d,]+)\)', line)
    cols = []
    for t in btns:
        col = np.zeros(n)
        xs = [int(x) for x in t.split(',')]
        for k in xs:
            if 0 <= k <n:
                col[k] = 1
        cols.append(col)
    a =np.column_stack(cols)
    nb = a.shape[1]
    c= np.ones(nb)
    # solve minimal presses- minimize sum(x) such that ax=b (parity constraints)
    cons=linearconstraint(a, b, b)
    integ =np.ones(nb)
    bnd= bounds(lb=0, ub=np.inf)
    r= milp(c=c, constraints=cons, integrality=integ, bounds=bnd)
    if r.success:
        res.append(int(round(r.fun)))

open("output-p2.txt", "w").write(str(sum(res)))
