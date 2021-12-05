'''
Advent of Code - Day 5
'''

import os
import pathlib
import collections

_LINES_FILE = 'day_5.txt'

raw_data = [line.strip().split(' -> ') for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                                     _LINES_FILE), 'r')]

lines = [(lambda line: [tuple(map(int, point.split(','))) for point in line])(line) for line in raw_data]

visited_points = []
visited_points_with_diagonals = []

for line in lines:
    (x1, y1), (x2, y2) = line
    if y1 == y2:
        if x1 > x2:
            start, stop = x2, x1
        else:
            start, stop = x1, x2
        for x in range(start, stop + 1):
            visited_points.append((x, y1))
            visited_points_with_diagonals.append((x, y1))
    elif x1 == x2:
        if y1 > y2:
            start, stop = y2, y1
        else:
            start, stop = y1, y2
        for y in range(start, stop + 1):
            visited_points.append((x1, y))
            visited_points_with_diagonals.append((x1, y))
    else:
        if x1 > x2:
            start_x, stop_x = x2, x1
            start_y = y2
            if y1 > y2:
                DIRECTION_Y = 1
            else:
                DIRECTION_Y = -1
        else:
            start_x, stop_x = x1, x2
            start_y = y1
            if y2 > y1:
                DIRECTION_Y = 1
            else:
                DIRECTION_Y = -1
        y = start_y
        for x in range(start_x, stop_x + 1):
            visited_points_with_diagonals.append((x, y))
            y += DIRECTION_Y

counter = collections.Counter(visited_points)
counter_with_diagonals = collections.Counter(visited_points_with_diagonals)
overlapping_points = len([x[0] for x in counter.most_common() if x[1] > 1])
overlapping_points_with_diagonals = len([x[0] for x in counter_with_diagonals.most_common() if x[1] > 1])
print(f'Overlapping points: {overlapping_points}')
print(f'Overlapping points (including diagonals): {overlapping_points_with_diagonals}')
