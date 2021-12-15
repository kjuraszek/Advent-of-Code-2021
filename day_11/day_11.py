'''
Advent of Code - Day 11
'''


import os
import pathlib


_DATA_FILE = 'day_11.txt'


def flash_neighbours(position, grid, matrix, queue):
    '''
    Function adds energy to all neigbours of flashed position
    and appends to list of positions to check.
    '''
    # pylint: disable=C0103
    x, y = position
    if x > 0 and y > 0 and not matrix[y - 1][x - 1]:
        grid[y - 1][x - 1] += 1
        queue.append((x - 1, y - 1))

    if y > 0 and not matrix[y - 1][x]:
        grid[y - 1][x] += 1
        queue.append((x, y - 1))

    if x < len(grid[0]) - 1 and y > 0 and not matrix[y - 1][x + 1]:
        grid[y - 1][x + 1] += 1
        queue.append((x + 1, y - 1))

    if x > 0 and y < len(grid[0]) - 1 and not matrix[y + 1][x - 1]:
        grid[y + 1][x - 1] += 1
        queue.append((x - 1, y + 1))

    if y < len(grid[0]) - 1 and not matrix[y + 1][x]:
        grid[y + 1][x] += 1
        queue.append((x, y + 1))

    if x < len(grid[0]) - 1 and y < len(grid[0]) - 1 and not matrix[y + 1][x + 1]:
        grid[y + 1][x + 1] += 1
        queue.append((x + 1, y + 1))

    if x > 0 and not matrix[y][x - 1]:
        grid[y][x - 1] += 1
        queue.append((x - 1, y))

    if x < len(grid[0]) - 1 and not matrix[y][x + 1]:
        grid[y][x + 1] += 1
        queue.append((x + 1, y))


energy_grid = [[int(value) for value in line.strip()] for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                                                    _DATA_FILE), 'r')]

FLASHED_100_STEP = 0
SYNCHRONIZED_FLASH_AT_STEP = 0
STEP = 0

while SYNCHRONIZED_FLASH_AT_STEP == 0:
    STEP += 1
    FLASHED_THIS_STEP = 0
    flash_matrix = [len(energy_grid[0]) * [False] for _ in energy_grid]
    energy_grid = [[int(value) + 1 for value in line] for line in energy_grid]
    to_visit = []
    for row_index, row in enumerate(energy_grid):
        for cell_index, cell in enumerate(row):
            if cell > 9:
                if (cell_index, row_index) not in to_visit:
                    to_visit.append((cell_index, row_index))
    while len(to_visit) > 0:
        current = to_visit.pop(0)
        if energy_grid[current[1]][current[0]] > 9 and not flash_matrix[current[1]][current[0]]:
            FLASHED_THIS_STEP += 1
            energy_grid[current[1]][current[0]] = 0
            flash_matrix[current[1]][current[0]] = True
            flash_neighbours(current, energy_grid, flash_matrix, to_visit)
    if STEP < 100:
        FLASHED_100_STEP += FLASHED_THIS_STEP
    if FLASHED_THIS_STEP == len(energy_grid[0]) ** 2:
        SYNCHRONIZED_FLASH_AT_STEP = STEP


print(f'Total flashes after 100 steps: {FLASHED_100_STEP}')
print(f'Synchornized flash at step: {SYNCHRONIZED_FLASH_AT_STEP}')
