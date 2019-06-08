from .img import img
import math
from .geometry import fit_points


def take(n, it):
    return [x for _, x in zip(range(n), it)]


def main(dir):
    width = 400
    height = 400

    confs = [
        (1.7, 1.7, 0.06, 1.2),
        (1.3, 1.7, 0.5, 1.4),
        (1.5, -1.8, 1.6, 0.9),
        (-1.4, 1.6, 1.0, 0.7),
    ]

    for index, conf in enumerate(confs):
        points = take(1000000, pickover(conf))

        i = img(width, height)
        for x, y in fit_points(points, width, height):
            i.addblack(x, y, 10)
        i.save(dir + '/pickover-' + str(index) + '.png')


def pickover(params):
    x = 0
    y = 0
    while True:
        (x, y) = next_point((x, y), params)
        yield (x, y)


def next_point(point, params):
    (x, y) = point
    (A, B, C, D) = params
    x2 = math.sin(A * y) + C * math.cos(A * x)
    y2 = math.sin(B * x) + D * math.cos(B * y)
    return (x2, y2)
