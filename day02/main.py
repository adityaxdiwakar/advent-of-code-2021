f = [(line[0], int(line.split(" ")[-1])) 
        for line in open("input.txt", "r").read().strip().split("\n")]
depth = horiz = 0
for (start, v) in f: 
    if start == "f": horiz += v
    else: depth += {"u": -1, "d": 1}[start] * v
print(depth*horiz)

aim = horiz = depth = 0
for (start, v) in f:
    if start == "f": horiz += v; depth += v * aim
    else: aim += {"u": -1, "d": 1}[start] * v
print(depth*horiz)
