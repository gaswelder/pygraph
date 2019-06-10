from .img import img
from . import geometry
import math
import itertools


def main(outdir):
    width = 400
    height = 400

    i = img(width, height)

    turtles = turtles_all_the_way_down(4, (width/2, height/2), 200, 0)
    for shape in itertools.islice(turtles, 100):
        i.polygon(shape)

    i.save(outdir + '/spiralgon.png')


def turtles_all_the_way_down(N, center, radius, angle):
    b = math.pi * (1/2 - 1/N)
    da = 0.1
    while True:
        yield geometry.regular_polygon(N, center, radius, angle)
        angle += da
        radius *= math.sin(b) / math.sin(b + da)
