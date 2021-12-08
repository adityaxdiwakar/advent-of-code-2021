f = [((spl := l.split(" | "))[0].split(" "), spl[1].split(" ")) 
        for l in open("input.txt").read().strip().split("\n")]

# part 1
print(sum([sum([1 for o in out if len(o) in [2, 3, 4, 7]]) for _, out in f]))

# part 2
total = 0
for patterns, outputs in f:
    patterns, c, = list(map(set, patterns)), [None] * 10
    for o in patterns:
        for k, v in {1:2, 4:4, 7:3, 8:7}.items():  
            if len(o) == v: c[k] = set(o)

    for o in patterns:
        if len(o) == 6:
            if c[1].issubset(o) and c[4].issubset(o): c[9] = o
            elif c[1].issubset(o): c[0] = o
            else: c[6] = o

        if len(o) == 5:
            if c[1].issubset(o): c[3] = o
            elif (c[8] - c[4]).issubset(o): c[2] = o
            else: c[5] = o

    base = 1000
    for o in outputs:
        total += (base * [i for i, a in enumerate(c) if a == set(o)][0])
        base //= 10
print(total)
