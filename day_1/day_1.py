'''
Advent of Code - Day 1
'''

import os
import pathlib


_MEASURES_FILE = 'day_1.txt'
_WINDOW_SIZE = 3
_MEASURES_V1 = [int(line.strip()) for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                                _MEASURES_FILE), 'r')]
_MEASURES_V2 = [sum(list(_MEASURES_V1[index:index + _WINDOW_SIZE]))
                for index, _ in enumerate(_MEASURES_V1)]


def compare_measures(measures_list):
    '''
    Function compares previous and next measure
    and retuns total increased measures
    '''
    increased = 0
    previous_measure = None
    for measure in measures_list:
        if previous_measure is None:
            previous_measure = measure
            continue
        if measure > previous_measure:
            increased += 1
        previous_measure = measure
    return increased


print(f'Increased measures (V1): {compare_measures(_MEASURES_V1)}')
print(f'Increased measures (V2): {compare_measures(_MEASURES_V2)}')
