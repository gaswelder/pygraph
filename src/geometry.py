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
