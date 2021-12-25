f = list(map(list, open("input.txt").read().strip().split("\n")))

cnt = 0
while (cnt := cnt + 1):
    has_moved = False

    moved_fish = set()
    cf = [row[:] for row in f]
    for i, row in enumerate(cf):
        for j, val in enumerate(row):
            if val == ">":
                idx = j + 1 if (j + 1) < len(f[0]) else 0
                if cf[i][idx] == ".": 
                    f[i][idx] = ">"
                    moved_fish.add((i, j))
                    has_moved = True

    for i, j in moved_fish: f[i][j] = "."

    moved_fish = set()
    cf = [row[:] for row in f]
    for i, row in enumerate(cf):
        for j, val in enumerate(row):
            if val == "v":
                idx = i + 1 if (i + 1) < len(f) else 0
                if f[idx][j] == ".": 
                    f[idx][j] = "v"
                    moved_fish.add((i, j))
                    has_moved = True

    for i, j in moved_fish: f[i][j] = "."

    if not has_moved:
        print("Part 1:", cnt)
        break

print("Part 2: Merry Christmas!")
