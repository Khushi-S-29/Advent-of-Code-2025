grid = [list(line.strip()) for line in open("input.txt") if line.strip()]
rows= len(grid)
cols = len(grid[0])
dirs= [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]

total_removed = 0
while True:
    to_remove = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '@':
                continue
            adj = 0
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == '@':
                        adj += 1
            if adj < 4:
                to_remove.append((r, c))
    if not to_remove:
        break
    for r, c in to_remove:
        grid[r][c] = '.'
    total_removed += len(to_remove)

open("output_p2.txt", "w").write(str(total_removed))
