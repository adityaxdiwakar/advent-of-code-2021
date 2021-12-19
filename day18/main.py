import itertools, ast, re
f = open("input.txt").read().strip().split("\n")

def get_idx_depths(chars):
    res, depth = [], 0
    for char in chars:
        depth += {"[": 1, "]": -1}.get(char, 0)
        res.append(depth)
    return res

def explode(res, start, stop):
    left = res[:start]
    right = res[stop+1:]

    middle = list(map(int, res[start + 1 : stop].split(",")))
    ml, mr = middle
    if match := re.search(r"\d+", right):
        l, r = match.start(), match.end()
        num = int(match.group(0))
        right = right[:l] + str(num + mr) + right[r:]

    if match := re.search(r"\d+", left[::-1]):
        l, r = -match.end(), -match.start()
        num = int(match.group(0)[::-1])
        left = left[:l] + str(num + ml) + left[r:]

    return left + "0" + right

def reduce(x):
    while True:
        fives = [i for i, v in enumerate(get_idx_depths(x)) if v == 5]
        if len(fives):
            x = explode(x, fives[0], x.index("]", fives[0]))

        elif match := re.search(r"\d\d+", x):
            num = int(match.group(0))
            l, r = match.start(), match.end()
            x = x[:l] + f"[{num//2},{num - num//2}]" + x[r:]

        else: return x

def add(x, y):
    return "[" + x + "," + y + "]"

def get_mag_str(s):
    lst = ast.literal_eval(s)
    def calc_mag(lst):
        if isinstance(lst, int): return lst
        return 3 * calc_mag(lst[0]) + 2 * calc_mag(lst[1])
    return calc_mag(lst)

res = f[0]
for num in f[1:]:
    res = reduce(add(res, num))
print(get_mag_str(res))


combs = list(itertools.combinations(f, 2))
max_mag = -1
for l, r in combs:
    max_mag = max(max_mag, get_mag_str(reduce(add(l, r))))
    max_mag = max(max_mag, get_mag_str(reduce(add(r, l))))
print(max_mag)
