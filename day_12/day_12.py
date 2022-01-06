'''
Advent of Code - Day 12
'''


import os
import pathlib


def search_paths_part_one(cave, path):
    '''
    Function searches for valid path until reaches the end.
    Function uses search method from part one.
    '''
    current_path = path[:]
    current_path.append(cave)
    if cave == 'end':
        FOUND_PATHS_PART_ONE.append(current_path)
    else:
        neighbours = get_neighbours(cave)
        for neighbour in neighbours:
            if neighbour.isupper() or neighbour == 'end' or (neighbour.islower() and neighbour not in current_path):
                search_paths_part_one(neighbour, current_path)


def search_paths_part_two(cave, path):
    '''
    Function searches for valid path until reaches the end.
    Function uses search method from part two.
    '''
    current_path = path[:]
    current_path.append(cave)
    if cave == 'end':
        FOUND_PATHS_PART_TWO.append(current_path)
    else:
        neighbours = get_neighbours(cave)
        small_cave_visited_twice = check_path_for_small_caves(current_path)
        for neighbour in neighbours:
            if neighbour.isupper() or neighbour == 'end' or not small_cave_visited_twice or neighbour not in current_path:
                search_paths_part_two(neighbour, current_path)


def check_path_for_small_caves(path):
    '''
    Function checks if any small cave was visited more than once.
    '''
    small_caves = [cave for cave in path if cave.islower()]
    small_caves = small_caves[1:]
    if len(small_caves) == len(set(small_caves)):
        return False
    return True


def get_neighbours(cave):
    '''
    Function gets the neighbours of the current cave.
    '''
    cave_connections = [connection for connection in CONNECTIONS if cave in connection]
    neighbours = []
    for connection in cave_connections:
        temp_connection = list(connection)
        temp_connection.pop(temp_connection.index(cave))
        neighbour = temp_connection.pop()
        if neighbour != 'start':
            neighbours.append(neighbour)
    return neighbours


_DATA_FILE = 'day_12.txt'

data = [line.strip() for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                   _DATA_FILE), 'r')]
CONNECTIONS = [tuple(connection.split('-')) for connection in data]
STARTING_CAVES = get_neighbours('start')
FOUND_PATHS_PART_ONE = []
FOUND_PATHS_PART_TWO = []

for start in STARTING_CAVES:
    starting_path = ['start']
    search_paths_part_one(start, starting_path)

for start in STARTING_CAVES:
    starting_path = ['start']
    search_paths_part_two(start, starting_path)

print(f'Paths found for part one: {len(FOUND_PATHS_PART_ONE)}')
print(f'Paths found for part two: {len(FOUND_PATHS_PART_TWO)}')
