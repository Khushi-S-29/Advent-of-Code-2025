pos = 50
hits = 0

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    direction = line[0]
    dist = int(line[1:])
    if direction == 'R':
        offset = (100 - pos) % 100
        first = offset or 100
        if dist >= first:
            hits += 1 + (dist - first) // 100
        pos = (pos + dist) % 100
    else:
        offset = pos % 100
        first = offset or 100
        if dist >= first:
            hits += 1 + (dist - first) // 100
        pos = (pos - dist) % 100

open("output_p2.txt", "w").write(str(hits))
