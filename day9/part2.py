data =open("input.txt").read().strip().splitlines()
pts=[]
for line in data:
    if ',' in line:
        x,y=map(int,line.split(','))
        pts.append((x, y))

if pts:
    n =len(pts)
    edges_h= []
    edges_v =[]
    for i in range(n):
        x1,y1 =pts[i]
        x2, y2= pts[(i + 1) % n]

        if x1== x2:
            edges_v.append((x1,min(y1,y2),max(y1,y2)))
        else:
            edges_h.append((y1,min(x1, x2), max(x1, x2)))
    max_area=0
    for i in range(n):
        x1, y1=pts[i]
        for j in range(i + 1, n):
            x2,y2= pts[j]
            min_x =min(x1, x2)
            max_x =max(x1,x2)
            min_y= min(y1, y2)
            max_y= max(y1, y2)
            w =max_x -min_x +1
            h =max_y-min_y +1
            area=w*h
            if area <=max_area:
                continue
            ok =True
            for px,py in pts:
                if min_x<px< max_x and min_y < py < max_y:
                    ok = False
                    break
            if not ok:
                continue
            for ey, ex1,ex2 in edges_h:
                if min_y < ey< max_y:
                    a = max(ex1, min_x)
                    b =min(ex2, max_x)
                    if a<b:
                        ok = False
                        break
            if not ok:
                continue
            for ex, ey1,ey2 in edges_v:
                if min_x <ex <max_x:
                    a = max(ey1,min_y)
                    b = min(ey2,max_y)
                    if a < b:
                        ok = False
                        break
            if not ok:
                continue
            cx =(min_x + max_x) / 2
            cy =(min_y + max_y) / 2
            ty =cy +1e-5
            tx =cx
            hits=0

            for k in range(n):
                x3,y3 =pts[k]
                x4, y4 = pts[(k + 1) % n]
                if (y3> ty) != (y4 > ty):
                    if x3 ==x4:
                        ix = x3
                    else:
                        continue
                    if tx <ix:
                        hits +=1
            if hits % 2 == 1:
                max_area = area
    open("output-p2.txt", "w").write(str(max_area))
