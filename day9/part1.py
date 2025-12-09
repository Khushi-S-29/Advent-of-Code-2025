pnts = []
for line in open("input.txt"):
    s =line.strip()
    if s:
        x,y = map(int, s.split(","))
        pnts.append((x, y))

best=0
n=len(pnts)

for i in range(n):
    x1,y1= pnts[i]
    for j in range(i+1, n):
        x2,y2=pnts[j]
        area=(abs(x1 -x2) +1) *(abs(y1 -y2)+ 1)
        if area >best:
            best =area
open("output_p1.txt", "w").write(str(best))
