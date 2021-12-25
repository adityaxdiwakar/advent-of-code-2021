from sys import argv
f = "input.txt" if len(argv) == 1 else argv[1]

# open file
file = open(f).read().strip().split("\n")

# get cube bounds 
pos_ = [l[l.find(" ")+1:].split(",") for l in file]
pos = [[list(map(int, c[2:].split(".."))) for c in l] for l in pos_]

# get states
states = [{"on": True, "off": False}[l[:l.find(" ")]] for l in file]

# part 1
on_cubes = set()

for state, bounds in zip(states, pos):
    ranges = [range(max(-50, a[0]), min(51, a[1] + 1)) for a in bounds]
    for x in ranges[0]:
        for y in ranges[1]:
            for z in ranges[2]:
                v = (x, y, z)
                if state: on_cubes.add(v)
                else: on_cubes.discard(v)
print(len(on_cubes))

# part 2
def intersect_1d(a, b):
    start_a, end_a = a # a1 <-> a2
    start_b, end_b = b # b1 <-> b2
    if start_b > end_a or start_a > end_b:
        return None
    nums = sorted([start_a, end_a, start_b, end_b])
    return [nums[1], nums[2]]

def intersect_3d(a, b):
    (start_xa, end_xa), (start_ya, end_ya), (start_za, end_za) = a
    (start_xb, end_xb), (start_yb, end_yb), (start_zb, end_zb) = b
    res = []
    for params in [ [(start_xa, end_xa), (start_xb, end_xb)],
                    [(start_ya, end_ya), (start_yb, end_yb)],
                    [(start_za, end_za), (start_zb, end_zb)]]:
        res.append(intersect_1d(*params))

    return res if all(res) else None

def volume(cube):
    (x1, x2), (y1, y2), (z1, z2) = cube[0]
    vol = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    for c in cube[1]: # compute volume of holes
        vol -= volume(c)
    return vol

def make_hole(cube, bounds):
    if (sect := intersect_3d(cube[0], bounds)):
        for i, sub_cube in enumerate(cube[1]):
            cube[1][i] = make_hole(sub_cube, sect)
        cube[1].append((sect, []))
    return cube

cubes = []
for state, bounds in zip(states, pos):
    for i, c in enumerate(cubes):
        cubes[i] = make_hole(c, bounds)
    if state:
        # each cuboid will be of form (bounds, [...holes...])
        cubes.append((bounds, []))

print(sum(volume(cube) for cube in cubes))

