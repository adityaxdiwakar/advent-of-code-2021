f = open("input.txt").read().strip().split("\n")
scores, valid_lines, illegal_chars = [], [], []
def line_check(line):
    stack = []
    for c in line:
        if c in (m := {"(": ")", "[": "]", "{": "}", "<": ">"}): stack.append(m[c])
        elif stack[-1] != c: 
            illegal_chars.append(c)
            return -1
        else: stack.pop()
    return stack

# part 1
for line in f: 
    if line_check(line) != -1: valid_lines.append(line)
print(sum([{")": 3, "]": 57, "}": 1197, ">": 25137}[c] for c in illegal_chars]))

# part 2
for line in valid_lines:
    lc, total = line_check(line)[::-1], 0
    for c in lc: total = total*5 + {")": 1, "]": 2, "}": 3, ">": 4}[c]
    scores.append(total)
print(sorted(scores)[len(scores) // 2])
