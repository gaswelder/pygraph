import png
from .geometry import triangles


def frange(x0, x1, step):
    x = x0
    while x < x1:
        yield x
        x += step
    yield x1


def darken(value, amount):
    if value < amount:
        return 0
    return value - amount


class line:
    def __init__(self, p1, p2):
        (x1, y1) = p1
        (x2, y2) = p2
        if x2 != x1:
            self.k = (y2 - y1) / (x2 - x1)
            self.b = y1 - self.k * x1
            self._x = None
        else:
            self._x = x1

    def x(self, y):
        if self._x is not None:
            return self._x
        return (y - self.b) / self.k


class img:
    def __init__(self, width=512, height=512):
        self.width = width
        self.height = height
        self.data = []
        for _ in range(0, self.height):
            for _ in range(0, self.width):
                self.data += [255, 255, 255]

    def _pixelpos(self, x, y):
        if x < 0 or x >= self.width:
            return -1
        if y < 0 or y >= self.height:
            return -1
        return (self.width * y + x) * 3

    def getpixel(self, x, y):
        pos = self._pixelpos(x, y)
        if pos < 0:
            raise IndexError(f"invalid (x, y): ({x}, {y})")
        return (self.data[pos], self.data[pos+1], self.data[pos+2])

    def putpixel(self, x, y, rgb):
        xi = round(x)
        yi = round(y)
        pos = self._pixelpos(xi, yi)
        if pos < 0:
            return
        for i in range(0, 3):
            self.data[pos + i] = rgb[i]

    def addblack(self, x, y, amount=1):
        xi = round(x)
        yi = round(y)
        (r, g, b) = self.getpixel(xi, yi)
        (r, g, b) = (
            darken(r, amount),
            darken(g, amount),
            darken(b, amount)
        )
        self.putpixel(xi, yi, (r, g, b))

    def line(self, p1, p2):
        (x0, y0) = p1
        (x1, y1) = p2
        n = 100
        dx = (x1 - x0) / n
        dy = (y1 - y0) / n
        for i in range(n + 1):
            self.putpixel(x0 + dx * i, y0 + dy * i, (0, 0, 0))

    def polyline(self, points):
        "Draws a sequence of lines through given points."
        points = list(points)
        pairs = zip(points, points[1:])
        for p in pairs:
            self.line(p[0], p[1])

    def polygon(self, points):
        "Draws a polygon with given points as vertices."
        pairs = zip(points, points[1:] + [points[0]])
        for p in pairs:
            self.line(p[0], p[1])

    def filled_polygon(self, points):
        self.polyline(points)
        for tr in triangles(points):
            self.filled_triangle(tr)

    def dot(self, point, color=(0, 0, 0), radius=2):
        (px, py) = point
        for x in frange(px - radius, px + radius, 1):
            for y in frange(py - radius, py + radius, 1):
                self.putpixel(x, y, color)

    def filled_triangle(self, triangle):
        # Figure out what vertex is at the top, bottom and between.
        [bottom, mid, top] = sorted(triangle, key=lambda p: p[1])

        # Split the triangle into two triangles with horizontal base.
        mid2 = (line(top, bottom).x(mid[1]), mid[1])

        # Fill the two triangles
        for y in frange(mid[1], top[1], 1):
            xx = [line(mid, top).x(y), line(mid2, top).x(y)]
            left = min(xx)
            right = max(xx)
            for x in frange(left, right, 1):
                self.putpixel(x, y, (0, 0, 0))
        for y in frange(bottom[1], mid[1], 1):
            xx = [line(mid, bottom).x(y), line(mid2, bottom).x(y)]
            left = min(xx)
            right = max(xx)
            for x in frange(left, right, 1):
                self.putpixel(x, y, (0, 0, 0))

    def save(self, path):
        with open(path, 'wb') as f:
            w = png.Writer(self.width, self.height)
            w.write_array(f, self.data)
            f.close()
