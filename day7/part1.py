grid = [line.rstrip("\n") for line in open("input.txt") if line.strip()]
rows=len(grid)
cols =len(grid[0])
start_row =None
start_col= None

for r in range(rows):
    c = grid[r].find("S")
    if c != -1:
        start_row = r
        start_col = c
        break
splits=0
beams={start_col}
for r in range(start_row + 1, rows):
    next_beams = set()
    for c in beams:
        if c <0 or c >=cols:
            continue
        ch= grid[r][c]
        if ch =='.':
            next_beams.add(c)
        elif ch== 'S':
            next_beams.add(c)
        elif ch == '^':
            splits += 1
            if c-1 >= 0:
                next_beams.add(c - 1)
            if c+1 < cols:
                next_beams.add(c + 1)
        else:
            next_beams.add(c)
    beams=next_beams

open("output_p1.txt", "w").write(str(splits))
