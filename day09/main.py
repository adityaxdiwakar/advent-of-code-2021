f = list(map(list, open("input.txt").read().strip().split("\n")))
z = [[1e5] * (len(f[0]) + 2) for _ in range(len(f) + 2)]
def perms(i, j): return [(i+1,j), (i-1, j), (i, j+1), (i, j-1)]
for i in range(len(f)):
    for j in range(len(f[i])): z[i+1][j+1] = int(f[i][j])
N, M, lows, basins = len(z), len(z[0]), [], []

# part 1
for i in range(1, N- 1):
    for j in range(1, M - 1):
        if min([z[r][c] for (r, c) in perms(i, j)]) > z[i][j]: 
            basins.append({(i, j)})
            lows.append(z[i][j])
print(sum(lows) + len(lows))

# part 2
def bfs(i, j, st):
    if z[i][j] in [9, 1e5] or not ((0 <= i <= N) and (0 <= j <= M)): return
    st.add((i, j))
    for (r, c) in perms(i, j): 
        if (r, c) in st: continue
        bfs(r, c, st)

for i in range(len(basins)):
    r, c = next(iter(basins[i]))
    bfs(r, c, basins[i])
total, lens = 1, sorted(list(map(len, basins)), reverse = True)
for l in lens[:3]: total *= l
print(total)
