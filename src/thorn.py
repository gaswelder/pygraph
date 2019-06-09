from .img import img
import random
import math


def main(outdir):
    width = 400
    height = 400

    params = [
        (0.102, -0.04),
        (1.098, 1.402),
        (9.984, 7.55),
        (0.662, 1.086),
        (-0.354, 0.162)
    ]
    for j, c in enumerate(params):
        values = thorn(c, width, height)
        normalize_values(values)

        i = img(width, height)
        for x, col in enumerate(values):
            for y, val in enumerate(col):
                i.putpixel(x, y, (val, val, val))
        i.save(outdir + f'/thorn-{j}.png')


def normalize_values(values):
    "Normalizes the table of values to the range of [0, 255]."
    lmin = 255
    lmax = 0

    for col in values:
        for val in col:
            lmin = min(lmin, val)
            lmax = max(lmax, val)

    for x, col in enumerate(values):
        for y, val in enumerate(col):
            values[x][y] = normalize(lmin, lmax, values[x][y])


def normalize(lmin, lmax, l):
    return round((l - lmin) / (lmax - lmin) * 255)


def thorn(c, width, height):
    "Generates a matrix of pixel values for thorn with parameter c."
    values = [[0 for y in range(width)] for x in range(height)]

    for x in range(width):
        for y in range(height):
            z = translate(x, y, width, height)
            values[x][y] = sample(z, c)
    return values


def translate(x, y, width, height):
    """translates image coordinates x and y to complex points"""
    p = math.pi
    return (-p + x * 2*p / width, -p + y * 2*p / height)


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
