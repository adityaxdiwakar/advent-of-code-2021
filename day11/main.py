# init 
f = [list(map(int, l)) for l in open("input.txt").read().strip().split("\n")]
perms = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]
num_flashes = [0, 0]

# func decl
def in_bounds(x, y): return 0 <= x < 10 and 0 <= y < 10
def spot_adder(x, y): 
    if f[x][y] >= 0: f[x][y] += 1
    if f[x][y] > 9: handle_flash(x, y)
def handle_flash(x, y, depth = 0):
    f[x][y] = -1; num_flashes[0] += 1
    for ax, ay in perms: 
        if not in_bounds((nx:=x+ax), (ny:=y+ay)): continue
        spot_adder(nx, ny)

# combined part 1 and part 2
for c in range(int(1e5)):
    for i, row in enumerate(f):
        for j, val in enumerate(row): spot_adder(i, j)
    f = [[a if a > 0 else 0 for a in row] for row in f]
    if num_flashes[0] - num_flashes[1] == 100:  
        print("Part 2:", c + 1)
        break
    if c == 99: print("Part 1:", num_flashes[0])
    num_flashes[1] = num_flashes[0]
