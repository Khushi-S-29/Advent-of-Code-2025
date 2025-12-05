ranges = []
for line in open("input.txt"):
    line = line.strip()
    if not line:
        break
    low, high = map(int, line.split("-"))
    ranges.append((low, high))
ranges.sort()
merged =[]
for low, high in ranges:
    if not merged or low > merged[-1][1] + 1:
        merged.append([low, high])
    else:
        merged[-1][1] = max(merged[-1][1], high)
total = sum(high - low + 1 for low, high in merged)

open("output_p2.txt", "w").write(str(total))
