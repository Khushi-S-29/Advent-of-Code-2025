g = {}
for line in open("input.txt"):
    line=line.strip()
    if not line: 
        continue
    a,b=line.split(":")
    g[a.strip()]=b.strip().split()

memo = {}
def dfs(x):
    if x in memo:
        return memo[x]
    if x=="out":
        return 1
    total =0
    for y in g.get(x,[]):
        total +=dfs(y)
    memo[x] = total
    return total

ans=dfs("you")
open("output-p1.txt","w").write(str(ans))
