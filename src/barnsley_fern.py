import random
from .img import img


def main(outdir):
    i = img(600, 600)
    p = (1, 1)
    for _ in range(1000000):
        (x, y) = p
        i.putpixel(300 + x * 50, 600 - y * 50, (0, 0, 0))
        p = f()(p)
    i.save(outdir + '/barnsley_fern.png')


def f():
    r = random.random()
    # (1), 1%
    # (2), 85%
    # (3), 7%
    # (4), 7%
    if r < 0.01:
        return f1
    r -= 0.01
    if r < 0.85:
        return f2
    r -= 0.85
    if r < 0.07:
        return f3
    return f4


def f1(point):
    (x, y) = point
    return (0, 0.16 * y)


def f2(point):
    (x, y) = point
    return (0.85 * x + 0.04 * y,
            -0.04 * x + 0.85 * y + 1.6)


def f3(point):
    (x, y) = point
    return (0.2 * x - 0.26 * y,
            0.23 * x + 0.22 * y + 1.6)


def f4(point):
    (x, y) = point
    return (-0.15 * x + 0.28 * y,
            0.26 * x + 0.24 * y + 0.44)
