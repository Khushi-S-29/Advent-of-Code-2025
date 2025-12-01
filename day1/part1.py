pos = 50
hits = 0

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    direction = line[0]
    dist = int(line[1:])
    if direction == 'L':
        pos = (pos - dist) % 100
    else:
        pos = (pos + dist) % 100
    if pos == 0:
        hits += 1

open("output_p1.txt", "w").write(str(hits))
