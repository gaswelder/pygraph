from .img import img
from .geometry import fit_points


def main(outdir):
    points = spread(fold('up', 15))
    points = fit_points(points, 400, 400)

    i = img(400, 400)
    i.polyline(points)
    i.save(outdir + '/dragon.png')


def fold(center, times):
    "Generates a list of fold directions for a strip folded 'times' times."
    if times == 0:
        return []
    if times == 1:
        return [center]
    return fold('down', times - 1) + [center] + fold('up', times - 1)


def spread(strip):
    "Converts a list of fold directions to polyline points."

    # Start at zero.
    # Use a "tutle" algorithm to obtain the points.
    points = [(0, 0)]
    t = Turtle((0, 0))
    for turn in strip:
        if turn == 'up':
            points.append(t.up())
        else:
            points.append(t.down())
    return points


class Turtle:
    def __init__(self, pos):
        self.dir = 'r'
        self.x, self.y = pos

    def up(self):
        diff = {
            'r': (0, 1),
            'l': (0, -1),
            'u': (-1, 0),
            'd': (1, 0)
        }[self.dir]

        self.x += diff[0]
        self.y += diff[1]

        self.dir = {'r': 'u',
                    'l': 'd',
                    'u': 'l',
                    'd': 'r'}[self.dir]
        return self.pos()

    def down(self):
        diff = {
            'r': (0, -1),
            'l': (0, 1),
            'u': (1, 0),
            'd': (-1, 0)
        }[self.dir]

        self.dir = {'r': 'd',
                    'l': 'u',
                    'u': 'r',
                    'd': 'l'}[self.dir]

        self.x += diff[0]
        self.y += diff[1]
        return self.pos()

    def pos(self):
        return (self.x, self.y)
