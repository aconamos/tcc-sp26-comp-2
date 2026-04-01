import sys


def ispointincircle(p_x: float, p_y: float, c_x: float, c_y: float, r: float):
    return ((p_x - c_x) ** 2 + (p_y - c_y) ** 2) < (r**2)


lines = [line.rstrip() for line in sys.stdin.readlines()]

l, w, n, r = [int(t) for t in lines[0].split(" ")]

left = (-l / 2, 0)
right = (l / 2, 0)
bottom = (0, -w / 2)
top = (0, w / 2)

crane_locs = []

for i in range(0, n):
    x, y = [int(z) for z in lines[i + 1].split(" ")]
    crane_locs.append((x, y))

crane_covers = [
    {
        "left": ispointincircle(left[0], left[1], crane[0], crane[1], r),
        "right": ispointincircle(right[0], right[1], crane[0], crane[1], r),
        "bottom": ispointincircle(bottom[0], bottom[1], crane[0], crane[1], r),
        "top": ispointincircle(top[0], top[1], crane[0], crane[1], r),
    }
    for crane in crane_locs
]
