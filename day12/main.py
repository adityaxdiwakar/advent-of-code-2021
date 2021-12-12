from collections import defaultdict
f = [l.split("-") for l in open("input.txt").read().strip().split("\n")]
total, edges = [0], defaultdict(lambda:[])
for u, v in f:
    edges[u].append(v)
    edges[v].append(u)

# part 1 and 2 combined, parametrized by `boundary`
def cnt_paths(visited, v, boundary):
    if v in visited:
        if v == "start": return

        max_ = max([0] + [v for k, v in visited.items() if k.islower()])
        if v.islower() and max_ >= boundary: return
        
    visited[v] += 1
    if v == "end": total[0] += 1
    else: [cnt_paths(visited, adj, boundary) for adj in edges[v]]

    visited[v] -= 1
    if visited[v] <= 0: del visited[v]

# part 1
cnt_paths(defaultdict(int), "start", 1)
print(prev := total[0])

# part 2
cnt_paths(defaultdict(int), "start", 2)
print(total[0] - prev)
