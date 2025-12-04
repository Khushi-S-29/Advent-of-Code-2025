grid = [line.strip() for line in open("input.txt") if line.strip()]
rows=len(grid)
cols = len(grid[0])
ans= 0
dirs = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),  (1, 1)]

for r in range(rows):
    for c in range(cols):
        if grid[r][c] != '@':
            continue
        adj=0
        for dr, dc in dirs:
            nr = r + dr
            nc= c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == '@':
                    adj += 1
        if adj <4:
            ans += 1

open("output_p1.txt", "w").write(str(ans))
