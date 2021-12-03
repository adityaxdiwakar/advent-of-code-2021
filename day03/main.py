f = open("input.txt").read().strip().split("\n")
cols = [[] for _ in range(len(f[0]))]
for line in f:
    for i, c in enumerate(line):
        cols[i].append(c)
bits = [str(int(x.count("1") > x.count("0"))) for x in cols]
obits = [str(int(x.count("1") < x.count("0"))) for x in cols]
print(int("".join(bits), 2) * int("".join(obits), 2))

nums = [0, 0]
nf = f[:]
for bit_pos in range(len(f[0])):
    col = []
    for line in nf: col.append(line[bit_pos])
    cmn = "1" if col.count("1") >= col.count("0") else "0"
    nf = [x for x in nf if x[bit_pos] == cmn]
    if len(nf) == 1: nums[0] = int(nf[0], 2); break

nf = f[:]
for bit_pos in range(len(f[0])):
    col = []
    for line in nf: col.append(line[bit_pos])
    cmn = "1" if col.count("1") < col.count("0") else "0"
    nf = [x for x in nf if x[bit_pos] == cmn]
    if len(nf) == 1: nums[1] = int(nf[0], 2); break

print(nums[0] * nums[1])
