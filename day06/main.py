from collections import defaultdict
f = list(map(int, open("input.txt").read().strip().split("\n")[0].split(",")))
def num_fish(num_days):
    days_left = defaultdict(int, {k: f.count(k) for k in f})
    for k in range(num_days):
        new_dict = defaultdict(int, {})
        for (left, num) in days_left.items():
            if left == 0:
                new_dict[8] = num
                left = 7
            new_dict[left - 1] += num
        days_left = new_dict
    print(sum(days_left.values()))

num_fish(80)
num_fish(256)

