'''
Advent of Code - Day 7
'''

import os
import pathlib
import collections

_DATA_FILE = 'day_7.txt'


def calculate_lowest_fuel(positions, method):
    '''
    Function to calculate minimum fuel needed based on crabs positions and calculation method.
    '''
    min_fuel = 0
    for index, crab_tuple in enumerate(positions):
        fuel = sum([calculate_step(method, abs(temp_tuple[0] - crab_tuple[0])) * temp_tuple[1]
                    for temp_index, temp_tuple in enumerate(positions) if not index == temp_index])
        if min_fuel == 0 or min_fuel > fuel:
            min_fuel = fuel
    return min_fuel


def calculate_step(method, absolute_index):
    '''
    Function to calculate step used in further calculations based on absolute difference between index values.
    '''
    step = ((absolute_index + 1) * absolute_index // 2 if method == 2
            else absolute_index)
    return step


with open(os.path.join(pathlib.Path(__file__).parent, _DATA_FILE), 'r') as data_file:  # pylint: disable=R1732,W1514 # noqa: E501
    raw_data = data_file.read()

crabs_positions = [int(crab_data) for crab_data in raw_data.split(',')]
most_common_crabs_positions = collections.Counter(crabs_positions).most_common()

print(f'Minimum fuel needed to reach horizontal position (V1): {calculate_lowest_fuel(most_common_crabs_positions, 1)}')
print(f'Minimum fuel needed to reach horizontal position (V2): {calculate_lowest_fuel(most_common_crabs_positions, 2)}')
