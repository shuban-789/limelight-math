#!/usr/bin/python3

import math

# Expected rotation: ~90 degrees or -90 degrees
# corners = [[228.0, 283.0], [217.0, 384.0], [540.0, 389.0], [514.0, 285.0]]

# Expected rotation: ~45 degrees
# corners = [[228.0, 235.0], [481.0, 418.0], [569.0, 324.0], [315.0, 173.0]]

# Expected rotation: ~0 degrees
corners = [[317.0, 158.0], [309.0, 377.0], [468.0, 378.0], [425.0, 157.0]]

distances = []

distance = lambda x1, y1, x2, y2: math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Corner of initiation is [228.0, 283.0]
def get_diag_pair(corners):
    reference = [corners[0][0], corners[0][1]]
    for corner in corners[1:]:
        d = distance(reference[0], reference[1], corner[0], corner[1])
        distances.append((d, corner, reference))
    distances.sort(reverse=True)
    return distances[0][1:]

# 4 corners should mean distances is of length 3. <diagonal, long, short>
def get_long_pair():
    return distances[1][1:]

def get_angle(long_pair):
    P1 = long_pair[0]
    P2 = long_pair[1]
    angle = math.atan2(abs(P2[1] - P1[1]), P2[0] - P1[0])
    return math.degrees(angle) - 90
    

print("Diagonal Corner Pair: " + str(get_diag_pair(corners)))
print("Long Side Corner Pair: " + str(get_long_pair()))
print("Angle: " + str(get_angle(get_long_pair())))