# helper collections
from collections import Counter, defaultdict
def get_soln():
    counts_s = sorted(counts.values())
    print(max(counts_s) - min(counts_s))

# parse
f = open("input.txt").read().strip().split("\n\n")
rules = {k:[k[0] + v, v + k[1]] 
        for k, v in [x.split(" -> ") for x in f[1].split("\n")]}
total_pairs, counts = {}, Counter(f[0])
for rule in rules:
    if (count := f[0].count(rule[:2])) > 0: total_pairs[rule[:2]] = count

for c in range(40):
    new_pairs = defaultdict(int)
    for k, v in total_pairs.items():
        if (np := rules.get(k)):
            for i in range(2): new_pairs[np[i]] += v
            counts[np[0][1]] += v
        else: new_pairs[k] += v
    total_pairs = new_pairs # copy for next step

    # part 1
    if c == 9: get_soln()
# part 2
get_soln()

