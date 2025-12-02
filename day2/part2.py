total = 0

for part in open("input.txt").read().strip().split(","):
    if not part:
        continue
    lo, hi = map(int, part.split("-"))
    for num in range(lo, hi + 1):
        s = str(num)
        length= len(s)
        for k in range(1, length//2 +1):
            if length %k != 0:
                continue
            block = s[:k]
            if block * (length // k) == s:
                total += num
                break

open("output_p2.txt", "w").write(str(total))
