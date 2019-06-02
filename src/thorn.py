from .img import img
import random
import math


def main(outdir):
    params = [
        (0.102, -0.04),
        (1.098, 1.402),
        (9.984, 7.55),
        (0.662, 1.086),
        (-0.354, 0.162)
    ]
    for j, c in enumerate(params):
        i = thorn(c)
        i.save(outdir + f'/thorn-{j}.png')


def normalize(lmin, lmax, l):
    return round((l - lmin) / (lmax - lmin) * 255)


def thorn(c):
    i = img(600, 600)
    lmin = 255
    lmax = 0
    for x in range(600):
        for y in range(600):
            z = translate(x, y)
            n = sample(z, c)
            lmin = min(lmin, n)
            lmax = max(lmax, n)
            i.putpixel(x, y, (n, n, n))

    for x in range(600):
        for y in range(600):
            p = i.getpixel(x, y)
            n = normalize(lmin, lmax, p[0])
            i.putpixel(x, y, (n, n, n))

    return i


def translate(x, y):
    """translates image coordinates x and y to complex points"""
    p = math.pi
    return (-p + x * 2*p / 600, -p + y * 2*p / 600)


def sample(z, c):
    # Spawn a series and see how long it takes for it to grow
    for steps, zn in enumerate(series(c, z)):
        if steps == 255 or (zn[0]**2 + zn[1]**2) > 10000:
            return steps


def series(c, z_start):
    z = next(c, z_start)
    while True:
        yield z
        z = next(c, z)


def next(c, z):
    (zre, zim) = z
    (cre, cim) = c

    # It's possible that sine or cosine will be zero,
    # leading to a division by zero. We simply patch it
    # by replacing zero with a very small non-zero number.
    cosim = math.cos(zim)
    sinre = math.sin(zre)
    if cosim == 0:
        cosim = 1e-20
    if sinre == 0:
        sinre = 1e-20

    return (zre / cosim + cre,  zim / sinre + cim)
