from math import floor, log10
import numpy as np

num = int(input("Enter number"))

def sqrt(num):
    num = int(np.sqrt(num))
    return num


n = sqrt(num)

justification = floor(log10(n * n) + 2)
canvas = [['' for j in range(n)] for i in range(n)]

dx, dy = (1, 0)
x, y = (0, 0)
for i in range(n * n):
    canvas[y][x] = str(i + 1).ljust(justification)

    if any((x + dx >= n, y - dy >= n, y - dy < 0, x + dx < 0)) or canvas[y - dy][x + dx]:
        dx, dy = dy, -dx

    x += dx
    y -= dy

print('\n'.join([''.join(c) for c in canvas]))

