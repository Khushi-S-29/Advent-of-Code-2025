from functools import lru_cache

grid = [line.rstrip("\n") for line in open("input.txt") if line.strip()]
rows= len(grid)
cols= len(grid[0])
start_r = None
start_c =None

for r in range(rows):
    c=grid[r].find("S")
    if c != -1:
        start_r = r
        start_c = c
        break

@lru_cache(maxsize=None)
def ways(r, c):
    if c < 0 or c>= cols or r >=rows:
        return 1
    ch= grid[r][c]
    if ch=='^':
        return ways(r, c-1) + ways(r,c+1)
    else:
        return ways(r + 1, c)
    
result=ways(start_r, start_c)

open("output_p2.txt", "w").write(str(result))
