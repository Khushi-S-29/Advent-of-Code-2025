total = 0

for line in open("input.txt"):
    line=line.strip()
    if not line:
        continue
    digits =list(line)
    n= len(digits)
    best = 0
    for i in range(n- 1):
        for j in range(i + 1, n):
            val = int(digits[i])*10 + int(digits[j])
            if val > best:
                best = val
    total += best

open("output_p1.txt", "w").write(str(total))
