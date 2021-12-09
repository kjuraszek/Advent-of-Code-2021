'''
Advent of Code - Day 9
'''

import os
import pathlib


_DATA_FILE = 'day_9.txt'


def check_is_basin_low_point(index_cell, index_row, cell, row, raw_data):  # pylint: disable=R0911
    '''
    Function checks if current cell is a lowest point by comparing its neighbours.

    If the cell is in the corner it has only 2 neighbours.
    If the cell is in the outline it has only 3 neighbours.
    If it is neither a corner and outline - it has 4 neigbours to check.
    If all neigbours are higher - a current cell is a low point and function returns True,
    otherwise False value is returned.
    '''
    if index_row == 0 and index_cell == 0:
        return all([cell < row[index_cell + 1], cell < raw_data[index_row + 1][index_cell]])
    if index_row == len(raw_data) - 1 and index_cell == 0:
        return all([cell < row[index_cell + 1], cell < raw_data[index_row - 1][index_cell]])
    if index_row == 0 and index_cell == len(raw_data) - 1:
        return all([cell < row[index_cell - 1], cell < raw_data[index_row + 1][index_cell]])
    if index_row == len(raw_data) - 1 and index_cell == len(raw_data) - 1:
        return all([cell < row[index_cell - 1], cell < raw_data[index_row - 1][index_cell]])
    if index_row == 0:
        return all([cell < row[index_cell + 1], cell < row[index_cell - 1], cell < raw_data[index_row + 1][index_cell]])
    if index_cell == 0:
        return all([cell < row[index_cell + 1], cell < raw_data[index_row - 1][index_cell], cell < raw_data[index_row + 1][index_cell]])
    if index_row == len(raw_data) - 1:
        return all([cell < row[index_cell + 1], cell < row[index_cell - 1], cell < raw_data[index_row - 1][index_cell]])
    if index_cell == len(raw_data) - 1:
        return all([cell < row[index_cell - 1], cell < raw_data[index_row - 1][index_cell], cell < raw_data[index_row + 1][index_cell]])

    return all([cell < row[index_cell - 1], cell < row[index_cell + 1],
                cell < raw_data[index_row - 1][index_cell], cell < raw_data[index_row + 1][index_cell]])


def check_neighbours(position_x, position_y, visited_cells, raw_data):
    '''
    Function checks neigbours of the cell with higher values to calculate the size of current basin.
    '''
    to_visit = []
    visited_cells.append((position_x, position_y))
    cell_value = raw_data[position_y][position_x]
    if(position_x - 1 >= 0 and raw_data[position_y][position_x - 1] < 9
       and cell_value < raw_data[position_y][position_x - 1]):
        to_visit.append((position_x - 1, position_y))
    if(position_x + 1 <= len(raw_data[0]) - 1 and raw_data[position_y][position_x + 1] < 9
       and cell_value < raw_data[position_y][position_x + 1]):
        to_visit.append((position_x + 1, position_y))
    if(position_y + 1 <= len(raw_data) - 1 and raw_data[position_y + 1][position_x] < 9
       and cell_value < raw_data[position_y + 1][position_x]):
        to_visit.append((position_x, position_y + 1))
    if(position_y - 1 >= 0 and raw_data[position_y - 1][position_x] < 9
       and cell_value < raw_data[position_y - 1][position_x]):
        to_visit.append((position_x, position_y - 1))
    for neighbour in to_visit:
        check_neighbours(neighbour[0], neighbour[1], visited_cells, raw_data)


data = [[int(value) for value in line.strip()] for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                                             _DATA_FILE), 'r')]

lowest_points = []
visited_basins_lengths = []
for row_index, row_value in enumerate(data):
    for location_index, location_value in enumerate(row_value):
        if check_is_basin_low_point(location_index, row_index, location_value, row_value, data):
            lowest_points.append(location_value + 1)
            visited = []
            check_neighbours(location_index, row_index, visited, data)
            visited_basins_lengths.append(len(set(visited)))

visited_basins_lengths.sort(reverse=True)
multiplied_visited_basins_lengths = 1
for length in visited_basins_lengths[:3]:
    multiplied_visited_basins_lengths *= length

print(f'Sum of the lowest points: {sum(lowest_points)}')
print(f'Multiplied 3 largest basins: {multiplied_visited_basins_lengths}')
