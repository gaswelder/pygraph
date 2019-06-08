from .img import img
import math
from .geometry import fit_points


def main(outdir):
    width = 400
    height = 400
    i = img(width, height)

    # Generate the shape
    points = take(100000, rossler(0.1, 0.1, 14))

    # Rotate it to get a better view
    points = [rotate_z(p, -math.pi/2) for p in points]
    points = [rotate_x(p, math.pi/3) for p in points]

    # Scale to fit the image
    points = fit_points(points, width, height)

    for p in points:
        i.addblack(p[0], p[1], 30)

    i.save(outdir + '/rossler.png')


def rossler(a, b, c):
    dt = 0.01
    (x, y, z) = (0, 0, 0)
    while True:
        yield (x, y, z)
        dx = (-y - z) * dt
        dy = (x + a * y) * dt
        dz = (b + z * (x - c)) * dt
        (x, y, z) = (x + dx, y + dy, z + dz)


def take(n, it):
    return [x for _, x in zip(range(n), it)]


def rotate_x(point, theta):
    (x, y, z) = point
    return (
        x,
        y * math.cos(theta) - z*math.sin(theta),
        y * math.sin(theta) + z*math.cos(theta)
    )


def rotate_y(point, theta):
    (x, y, z) = point
    return (
        x * math.cos(theta) + z * math.sin(theta),
        y,
        -x * math.sin(theta) + z * math.cos(theta)
    )


def rotate_z(point, theta):
    (x, y, z) = point
    return (
        x*math.cos(theta) - y*math.sin(theta),
        x*math.sin(theta) + y*math.cos(theta),
        z
    )
