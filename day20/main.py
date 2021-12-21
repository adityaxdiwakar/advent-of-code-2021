enhance, img  = open("input.txt").read().strip().split("\n\n")
enhance = enhance.replace("#", "1").replace(".", "0")
img = [list(line.replace("#", "1").replace(".", "0"))
        for line in img.split("\n")]

def print_img(img):
    for line in img: 
        print("".join(line).replace("1", "#").replace("0", "."))

def inr(x, y): 
    return 0 <= x < len(img) and 0 <= y < len(img[0])

adjs = [(x, y) for x in range(-1, 2) for y in range(-1, 2)]

ad = 50 * 4
new_img = [["0"] * (len(img[0]) + ad) for _ in range(len(img) + ad)]

for i in range(len(img)):
    for j in range(len(img[0])):
        new_img[i+ad//2][j+ad//2] = img[i][j]
img = new_img


def get_adj_bin(x, y, i):
    bin_str = []
    for ax, ay in adjs:
        if not inr(x + ax, y + ay): 
            bin_str.append("01"[i%2 and enhance[0] == "1"])
        else: 
            bin_str.append(img[x+ax][y+ay])
    return int("".join(bin_str), 2)

def replace_pixel(x, y, new_img, i):
    idx = get_adj_bin(x, y, i)
    new_img[x][y] = enhance[idx]

def count_img(img): 
    print(sum([line.count("1") for line in img]))

def enhance_img():
    global img
    for i in range(50):
        new_img = [line[:] for line in img]
        for x in range(len(img)):
            for y in range(len(img[0])):
                replace_pixel(x, y, new_img, i)
        img = new_img
        if i in [1, 49]: count_img(img)

img = enhance_img()
