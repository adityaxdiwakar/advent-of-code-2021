# helpers
import heapq
def get_adj(x, y): return [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

# parse
in_ = open("input.txt").read().strip().split("\n")
in_ = [list(map(int, list(l))) for l in in_]

# part one
def part_one(f):
    q, cs = [(0, 0, 0)], {}
    cost, x, y = heapq.heappop(q)
    while not (x == len(f) - 1 and y == len(f[0]) - 1):
        for nx, ny in get_adj(x, y):
            if not(0 <= nx < len(f) and 0 <= ny < len(f[0])): continue
            nc = cost + f[nx][ny]
            if (nx, ny) not in cs or nc < cs[nx, ny]:
                cs[nx, ny] = nc
                heapq.heappush(q, (nc, nx, ny))
        cost, x, y, = heapq.heappop(q)
    print(cost)

def part_two(f):
    q, cs = [(0, 0, 0)], {}
    cost, x, y = heapq.heappop(q)
    while not (x == 5 * len(f) - 1 and y == 5 * len(f[0]) - 1):
        for nx, ny in get_adj(x, y):
            if not(0 <= nx < 5*len(f) and 0 <= ny < 5*len(f[0])): continue
            roll_over = f[nx % len(f)][ny % len(f[0])] + nx // len(f) + ny // len(f[0])
            if roll_over > 9: roll_over = roll_over - 9
            nc = cost + roll_over 
            if (nx, ny) not in cs or nc < cs[nx, ny]:
                cs[nx, ny] = nc
                heapq.heappush(q, (nc, nx, ny))
        cost, x, y, = heapq.heappop(q)
    print(cost)
     

part_one(in_)
part_two(in_)
