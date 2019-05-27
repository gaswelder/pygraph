from .img import img
import math


def darken(value, amount=1):
    if value < amount:
        return 0
    return value - amount


def addblack(pixel):
    (r, g, b) = pixel
    return (darken(r), darken(g), darken(b))


def next_point(point, params):
    (x, y) = point
    (A, B, C, D) = params
    x2 = math.sin(A * y) + C * math.cos(A * x)
    y2 = math.sin(B * x) + D * math.cos(B * y)
    return (x2, y2)


def pickover_attractor(params, filename):
    i = img(600, 600)
    x = 0
    y = 0
    for _ in range(0, 10000000):
        (x, y) = next_point((x, y), params)
        rx = int(100 * x) + 300
        ry = int(100 * y) + 300
        i.putpixel(rx, ry, addblack(i.getpixel(rx, ry)))
    i.save(filename)


def main(dir):
    confs = [
        (1.7, 1.7, 0.06, 1.2),
        (1.3, 1.7, 0.5, 1.4),
        (1.5, -1.8, 1.6, 0.9),
        (-1.4, 1.6, 1.0, 0.7),
    ]

    for [conf, index] in list(zip(confs, range(len(confs)))):
        pickover_attractor(conf, dir + '/pickover-' + str(index) + '.png')
