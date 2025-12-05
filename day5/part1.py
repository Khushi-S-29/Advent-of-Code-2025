lines =[line.strip() for line in open("input.txt")]
ranges =[]
i= 0
while i <len(lines) and lines[i] != "":
    low,high =map(int, lines[i].split("-"))
    ranges.append((low, high))
    i +=1
available = [int(x) for x in lines[i+1:] if x]
fresh = 0
for id in available:
    for low, high in ranges:
        if low <= id <= high:
            fresh += 1
            break

open("output_p1.txt", "w").write(str(fresh))
