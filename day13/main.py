f = open("input.txt").read().strip().split("\n\n")
dots, folds = [list(map(int, x.split(","))) 
        for x in f[0].split("\n")], [x[x.rfind("=") - 1:] for x in f[1].split("\n")]
dot_cols, dot_rows = max([x[0] for x in dots]), max([x[1] for x in dots])
grid = [["." for _ in range(dot_cols + 1)] for _ in range(dot_rows + 1)]
for c, r in dots: grid[r][c] = "#"

# folds
for c, fold in enumerate(folds):
    if fold[0] == "y":
        #fold down to up
        y_c = int(fold[fold.rfind("=") + 1:])
        for i, line in enumerate(grid):
            for j, val in enumerate(line):
                if i > y_c and grid[i][j] == "#": grid[2*y_c - i][j] = "#"
        grid = grid[:y_c]
    
    if fold[0] == "x":
        x_c = int(fold[fold.rfind("=") + 1:])
        for i, line in enumerate(grid):
            for j, val in enumerate(line):
                if j > x_c and grid[i][j] == "#": grid[i][2*x_c - j] = "#"
        grid = [line[:x_c] for line in grid]

    # part 1 solution
    if c == 0: print("Part 1:", sum([x.count("#") for x in grid]))

# part 2 solution
for line in grid: print("".join(line))
