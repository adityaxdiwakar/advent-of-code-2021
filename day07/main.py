from statistics import mean, median
f = list(map(int, open("input.txt").read().strip().split("\n")[0].split(",")))

# part 1
med_ = median(f)
print(sum([int(abs(a - med_)) for a in f]))

# part 2
mean_ = int(mean(f))
print(sum([((b := abs(a - mean_)) * (b + 1)) // 2 for a in f]))
