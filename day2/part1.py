total = 0

for part in open("input.txt").read().strip().split(","):
    if not part:
        continue
    low, high = map(int, part.split("-"))
    for num in range(low, high + 1):
        s= str(num)
        if len(s) % 2 != 0:
            continue
        half = len(s) // 2
        left = s[:half]
        right = s[half:]
        if left == right:
            total += num

open("output_p1.txt", "w").write(str(total))
