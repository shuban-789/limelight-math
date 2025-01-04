#!/usr/bin/python3
import math

# Expected rotation: ~90 degrees or -90 degrees
# corners = [[228.0, 283.0], [217.0, 384.0], [540.0, 389.0], [514.0, 285.0]]

# Expected rotation: ~45 degrees
corners = [[228.0, 235.0], [481.0, 418.0], [569.0, 324.0], [315.0, 173.0]]

# Expected rotation: ~0 degrees
# corners = [[317.0, 158.0], [309.0, 377.0], [468.0, 378.0], [425.0, 157.0]]

distances = []

distance = lambda x1, y1, x2, y2: math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def get_diag_pair(corners):
    n = len(corners)
    for i in range(n):
        for j in range(i):
            d = distance(corners[i][0], corners[i][1], corners[j][0], corners[j][1])
            distances.append((d, corners[i], corners[j]))
    distances.sort(reverse=True)
    print(distances)
    return distances[0][1:]

def get_long_pair():
    diag_pair = distances[0][1:]
    long_side_candidates = []

    for entry in distances[1:]:
        pair = entry[1:]
        if diag_pair[0] in pair or diag_pair[1] in pair:
            long_side_candidates.append(pair)
    
    long_side_candidates.sort(key=lambda p: distance(p[0][0], p[0][1], p[1][0], p[1][1]), reverse=True)

    return long_side_candidates[0]

def get_angle(long_pair):
    P1 = long_pair[0]
    P2 = long_pair[1]
    angle = math.atan2(abs(P2[1] - P1[1]), P2[0] - P1[0])
    return math.degrees(angle) - 90
    

print("Diagonal Corner Pair: " + str(get_diag_pair(corners)))
print("Long Side Corner Pair: " + str(get_long_pair()))
print("Angle: " + str(get_angle(get_long_pair())))