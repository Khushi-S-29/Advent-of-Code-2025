lines = [line.rstrip("\n") for line in open("input.txt")]
rows = len(lines)
cols= max(len(line) for line in lines)
grid =[list(line.ljust(cols)) for line in lines]

def column_is_blank(c: int) -> bool:
    for r in range(rows):
        if grid[r][c] != " ":
            return False
    return True
blocks =[]
c= 0
while c< cols:
    while c < cols and column_is_blank(c):
        c +=1
    if c >=cols:
        break
    start = c
    while c< cols and not column_is_blank(c):
        c += 1
    end = c-1
    blocks.append((start, end))
total = 0

for start,end in blocks:
    op_row = rows - 1
    op = None
    for col in range(start, end + 1):
        ch = grid[op_row][col]
        if ch in "+*":
            op = ch
            break
    nums = []
    for col in range(start, end + 1):
        digits= []
        for r in range(rows - 1):
            ch= grid[r][col]
            if ch.isdigit():
                digits.append(ch)
        if digits:
            nums.append(int("".join(digits)))
    if not nums or op is None:
        continue
    if op== "+":
        value = sum(nums)
    else:
        value= 1
        for x in nums:
            value *= x
    total+= value

open("output_p2.txt", "w").write(str(total))
