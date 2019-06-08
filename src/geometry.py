import math


def triangles(polygon):
    """Splits a polygon into triangles."""

    if len(polygon) < 3:
        return []

    # Find the leftmost point
    left_pos = -1
    for i, p in enumerate(polygon):
        if left_pos == -1 or p[0] < p[left_pos]:
            left_pos = i

    # Take the leftmost point and its two neighbours
    left = polygon[left_pos]
    a = polygon[left_pos - 1]
    b = polygon[left_pos + 1]

    rest = polygon[:left_pos] + polygon[left_pos+1:]
    return [[a, left, b]] + triangles(rest)


def pentagon(center, radius, start_angle=0):
    """Returns a list of pentagon corner points"""
    points = []
    (cx, cy) = center
    for j in range(5):
        angle = j * 2 * math.pi/5 + start_angle
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        points.append((x, y))
    return points


def fit_points(points, width, height):
    """Scales the points so that they all fit in the given width and height"""
    margin = 10
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    # minx * k + c = left
    # maxx * k + c = right
    xmax = max(xs)
    xmin = min(xs)
    ymax = max(ys)
    ymin = min(ys)
    xleft = margin
    xright = width - margin
    yleft = margin
    yright = height - margin
    kx = (xright - xleft) / (xmax - xmin)
    ky = (yright - yleft) / (ymax - ymin)

    k = min(kx, ky)
    cx = 0.5 * (width - k*(xmax + xmin))
    cy = 0.5 * (height - k*(ymax + ymin))

    return zip(
        [k*x + cx for x in xs],
        [k*y + cy for y in ys]
    )
