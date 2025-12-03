def best12(s):
    need = 12
    stack =[]
    rem = len(s)
    for c in s:
        while stack and stack[-1] < c and len(stack) - 1 + rem >= need:
            stack.pop()
        if len(stack) < need:
            stack.append(c)
        rem-= 1
    return int("".join(stack))

total = 0

for line in open("input.txt"):
    line = line.strip()
    if not line:
        continue
    total+=best12(line)

open("output_p2.txt", "w").write(str(total))
