from .img import img
from . import geometry
import math


def main(outdir):
    width = 400
    height = 400
    i = img(width, height)

    # Instead of operating on points, use
    # tuples describing the pentagons: (center, radius, angle).

    # Start with a single pentagon
    # then replace pentagons with smaller ones a few times.
    pentagons = [((width/2, height/2), width/2-20, 0)]
    for _ in range(4):
        pentagons = replace(pentagons)

    # Render the result
    for spec in pentagons:
        render_pentagon(i, spec)

    i.save(outdir + '/pentaflake.png')


def replace(specs):
    new_list = []
    for spec in specs:
        new_list += replace_pentagon(spec)
    return new_list


def pentagon(c, r, angle):
    return geometry.regular_polygon(5, c, r, angle)


def replace_pentagon(pentagon_spec):
    (current_center, current_radius, angle) = pentagon_spec
    r = current_radius / (1 + 2 * math.cos(math.pi / 5))

    smaller_pentagons = []
    for p in pentagon(current_center, current_radius - r, 0):
        smaller_pentagons.append((p, r, angle))
    smaller_pentagons.append((current_center, r, angle + math.pi / 5))
    return smaller_pentagons


def render_pentagon(i, spec):
    (center, radius, angle) = spec
    points = pentagon(center, radius, angle)
    i.polygon(points)
    i.filled_polygon(points)
