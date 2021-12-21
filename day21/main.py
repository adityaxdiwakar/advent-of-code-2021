from sys import argv
f = "input.txt" if len(argv) == 1 else argv[1]

pos = [int(x[x.rfind(":") + 2:]) for x in open(f).read().split("\n")[:-1]]
save = pos[:]

# part 1
die_cnt = 0
def dice():
    global die_cnt
    die_cnt = die_cnt + 1
    return (die_cnt - 1) % 100 + 1

scores = [0] * len(pos)
def game():
    while True:
        for i in range(len(pos)):
            pos[i] += sum(dice() for _ in range(3))
            pos[i] = (pos[i] - 1) % 10 + 1
            
            scores[i] += pos[i]
            if scores[i] >= 1000: return i

loss_score = scores[not game()]
print(die_cnt * loss_score)

# part 2
pos = save[:] # load position save

# get dice possibilities for 3 roles
from collections import Counter; from itertools import product
cntr = dict(Counter(map(sum, product([1, 2, 3], repeat=3))))

from functools import cache

@cache # need memoization, lots of repeated function calls
def dirac_game(pos1, pos2, score1, score2):
    if score2 >= 21: return 0, 1

    wins = [0, 0]
    for (move, num) in cntr.items():
        new_pos = (pos1 - 1 + move) % 10 + 1
        # swap scores and positions and play the same game (sub-problem)
        w2, w1 = dirac_game(pos2, new_pos, score2, score1 + new_pos)

        # scale wins by num as that's how many times this dice combo showed up
        wins = wins[0] + w1 * num, wins[1] + w2 * num
    return wins

print(max(dirac_game(pos[0], pos[1], 0, 0)))
