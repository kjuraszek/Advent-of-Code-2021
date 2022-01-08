'''
Advent of Code - Day 15
'''


import os
import pathlib
import queue


def get_neighbours(tile, current_map):
    '''
    Function returns neighbours for current tile.
    '''
    position_x, position_y = tile
    map_size = len(current_map)
    neighbours = []
    if position_x > 0:
        neighbours.append((position_x - 1, position_y))
    if position_x < map_size - 1:
        neighbours.append((position_x + 1, position_y))
    if position_y > 0:
        neighbours.append((position_x, position_y - 1))
    if position_y < map_size - 1:
        neighbours.append((position_x, position_y + 1))
    return neighbours


def get_tile_risk(tile, current_map):
    '''
    Function returns risk for current tile.
    '''
    position_x, position_y = tile
    return current_map[position_y][position_x]


def count_paths_risk(current_map, starting_tile=(0, 0)):
    '''
    Function counts minimal risk for all tiles.
    '''
    # this algorithm isn't quite efficient, especially for the larger map
    ending_tile = (len(current_map) - 1, len(current_map) - 1)
    tiles_risk = {}
    for index_y, row in enumerate(current_map):
        for index_x, _ in enumerate(row):
            tiles_risk[(index_x, index_y)] = float('inf')
    tiles_risk[starting_tile] = 0
    visited_tiles = []
    tiles_queue = queue.PriorityQueue()
    tiles_queue.put((0, starting_tile))
    while not tiles_queue.empty():
        _, current_tile = tiles_queue.get()
        visited_tiles.append(current_tile)
        neighbours = get_neighbours(current_tile, current_map)
        for neighbour in neighbours:
            if neighbour not in visited_tiles:
                new_risk = tiles_risk[current_tile] + get_tile_risk(neighbour, current_map)
                old_risk = tiles_risk[neighbour]
                if new_risk < old_risk:
                    tiles_risk[neighbour] = new_risk
                    tiles_queue.put((new_risk, neighbour))
    return tiles_risk[ending_tile]


def prepare_large_map():
    '''
    Function prepares larger map based on the smaller map.
    '''
    large_map = []
    for i in range(_LARGE_MAP_SIZE):
        for row in MAP:
            new_row = []
            for j in range(_LARGE_MAP_SIZE):
                new_row += [element + i + j for element in row]
            new_row = list(map(lambda x: x if x < 10 else x - 9, new_row))
            large_map.append(new_row)
    return large_map


_DATA_FILE = 'day_15.txt'
_LARGE_MAP_SIZE = 5

data = [line.strip() for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                   _DATA_FILE), 'r')]

MAP = [[int(tile) for tile in row] for row in data]
LARGE_MAP = prepare_large_map()

print(f'Lowest risk path for the first map: {count_paths_risk(MAP)}')
print(f'Lowest risk path for the second (larger) map:{count_paths_risk(LARGE_MAP)}')
