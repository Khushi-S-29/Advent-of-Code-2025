g={}
for line in open("input.txt"):
    line =line.strip()
    if not line:
        continue
    a,b =line.split(":")
    g[a.strip()]=b.strip().split()

memo ={}
def dfs(x, sd, sf):
    k= (x, sd, sf)
    if k in memo:
        return memo[k]
    if x =="dac":
        sd=True
    if x=="fft":
        sf=True
    if x== "out":
        memo[k]= 1 if (sd and sf) else 0
        return memo[k]
    total =0
    for y in g.get(x,[]):
        total+=dfs(y, sd, sf)
    memo[k]= total
    return total

ans=dfs("svr", False, False)
open("output-p2.txt","w").write(str(ans))
