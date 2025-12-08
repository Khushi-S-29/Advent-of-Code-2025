coords = []
for line in open("input.txt"):
    s= line.strip()
    if s:
        x, y,z =map(int, s.split(","))
        coords.append((x, y, z))
n =len(coords)

edges = []
for i in range(n):
    x1, y1, z1 = coords[i]
    for j in range(i + 1, n):
        x2, y2, z2 = coords[j]
        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        d2 = dx*dx + dy*dy + dz*dz
        edges.append((d2, i, j))
edges.sort(key=lambda e: e[0])
parent = list(range(n))
size=[1] * n

def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra==rb:
        return False
    if size[ra]<size[rb]:
        ra, rb = rb, ra
    parent[rb]=ra
    size[ra] += size[rb]
    return True

components=n
last_i=last_j = None
for d2,i,j in edges:
    if union(i, j):
        components-= 1
        if components == 1:
            last_i = i
            last_j = j
            break

xi=coords[last_i][0]
xj =coords[last_j][0]
open("output_p2.txt", "w").write(str(xi * xj))
