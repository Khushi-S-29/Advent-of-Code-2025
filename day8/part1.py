coords = []
for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    x, y, z = map(int, line.split(","))
    coords.append((x, y, z))
n= len(coords)
edges= []
for i in range(n):
    x1,y1, z1 = coords[i]
    for j in range(i + 1, n):
        x2, y2, z2 = coords[j]
        dx = x1 -x2
        dy = y1- y2
        dz = z1- z2
        d2 = dx*dx +dy*dy+ dz *dz
        edges.append((d2, i,j))
edges.sort(key=lambda e: e[0])
parent = list(range(n))
size = [1] * n
def find(x):
    while parent[x]!=x:
        parent[x] =parent[parent[x]]
        x= parent[x]
    return x

def union(a, b):
    ra=find(a)
    rb=find(b)
    if ra== rb:
        return
    if size[ra] <size[rb]:
        ra,rb=rb, ra
    parent[rb] = ra
    size[ra] += size[rb]

limit=min(1000, len(edges))
for k in range(limit):
    l,i,j = edges[k]
    union(i, j)

component_sizes = []
for i in range(n):
    if parent[i] == i:
        component_sizes.append(size[i])

component_sizes.sort(reverse=True)
res= 1
for s in component_sizes[:3]:
    res*=s
open("output_p1.txt", "w").write(str(res))
