f = open("input.txt").read().strip().split("\n")[0]
x_bounds= list(map(int, f[f.find("x=") + 2:f.rfind(",")].split("..")))
y_bounds= list(map(int, f[f.find("y=") + 2:].split("..")))

def inr(x, y): 
    return x_bounds[0] <= x <= x_bounds[1] and y_bounds[0] <= y <= y_bounds[1]

def past(x, y):
    return x > x_bounds[1] or y < y_bounds[0]

def step(x, y, xv, yv):
    def to_zero(v): return v - 1 if v > 0 else (v if v == 0 else v + 1)
    return x + xv, y + yv, to_zero(xv), yv - 1

# part 1
print((y_bounds[0] * (y_bounds[0] + 1)) // 2)


total = 0
for cxv in range(x_bounds[1] + 2):
    for cyv in range(y_bounds[0] - 2, 1000):
        steps = x = y = 0
        cur_xv, cur_yv = cxv, cyv
        while not past(x, y):
            x, y, cur_xv, cur_yv = step(x, y, cur_xv, cur_yv)
            if inr(x, y): 
                total += 1
                break
            if steps > 50: break
print(total)
