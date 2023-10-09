import numpy as np


def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def point_to_segment_distance(px, py, x1, y1, x2, y2, segment_length):
    if segment_length == 0:
        return distance(px, py, x1, y1)

    # Calculate the vector components from (x1, y1) to (px, py)
    dx1 = px - x1
    dy1 = py - y1

    # Calculate the vector components from (x1, y1) to (x2, y2)
    dx2 = x2 - x1
    dy2 = y2 - y1

    # Calculate the dot product of the two vectors
    dot_product = dx1 * dx2 + dy1 * dy2

    if dot_product < 0:
        # The point is closest to the first endpoint (x1, y1)
        return distance(px, py, x1, y1)

    if dot_product > segment_length ** 2:
        # The point is closest to the second endpoint (x2, y2)
        return distance(px, py, x2, y2)

    # The point is closest to some point along the line segment.
    # Use the formula for the distance from a point to a line.
    distance_to_line = np.abs(dx1 * dy2 - dx2 * dy1) / segment_length

    return distance_to_line

def kraemer_points_on_triangle(v, n):
    # Generate random points within the triangle defined by vertices v
    x = np.sort(np.random.rand(2, n), axis=0)
    return np.column_stack([x[0], x[1] - x[0], 1.0 - x[1]]) @ v

v = np.array([(33, 32), (51, 9), (2, 3)])

runs = 100
points = kraemer_points_on_triangle(v, runs)

# Calculate the expected distance
expected_distances = []
segments = [
    distance(v[0, 0], v[0, 1], v[1, 0], v[1, 1]),
    distance(v[1, 0], v[1, 1], v[2, 0], v[2, 1]),
    distance(v[2, 0], v[2, 1], v[0, 0], v[0, 1]),
]
for point in points:
    distance_to_sides = [
        point_to_segment_distance(point[0], point[1], v[0, 0], v[0, 1], v[1, 0], v[1, 1], segments[0]),
        point_to_segment_distance(point[0], point[1], v[1, 0], v[1, 1], v[2, 0], v[2, 1], segments[1]),
        point_to_segment_distance(point[0], point[1], v[2, 0], v[2, 1], v[0, 0], v[0, 1], segments[2])
    ]
    expected_distances.append(min(distance_to_sides))

mean_distance = np.mean(expected_distances)
print(mean_distance)
