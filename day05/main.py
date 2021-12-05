# grid counter
def compute_total(s = 0):
    for r in grid: 
        for c in r:
            if c > 1: s += 1
    print(s)

# open and parse file
f = [[tuple(map(int, x.split(","))) for x in d.split(" -> ")] 
        for d in open("input.txt").read().strip().split("\n")]

# compute boundaries and create grid
def tp_max(x, i): return max(x[0][i], x[1][i])
max_x, max_y = [max(f, key=lambda x: tp_max(x, i))[0][i] for i in range(2)]
grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

# find horiz/vert interesections
for ((x1, y1), (x2, y2)) in f:
    if x1 != x2 and y1 != y2: continue # only consider horiz/vert
    dist, x, y = abs(x1 - x2) if x1 != x2 else abs(y1 - y2), x1, y1
    for _ in range(dist + 1):
        grid[x][y] += 1
        x += 0 if x1 == x2 else [-1, 1][x2 > x1]
        y += 0 if y1 == y2 else [-1, 1][y2 > y1]
compute_total()

# now also find diag
for ((x1, y1), (x2, y2)) in f:
    if x1 == x2 or y1 == y2: continue
    dist, x, y = abs(x1 - x2), x1, y1
    for _ in range(dist + 1):
        grid[x][y] += 1
        x += [1, -1][x1 > x2]
        y += [1, -1][y1 > y2]
compute_total()
