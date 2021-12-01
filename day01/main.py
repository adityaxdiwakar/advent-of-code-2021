# open file, parse lines as integers
f = [int(x) for x in open("input.txt", "r").read().strip().split("\n")]
# compare adjacent items using zip
print(sum([b > a for (a, b) in zip(f, f[1:])]))
# moving a sliding window removes first, adds last, compare for inc/dec
print(sum([b > a for (a, b) in zip(f[:-3], f[3:])]))
