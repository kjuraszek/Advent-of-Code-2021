'''
Advent of Code - Day 6
'''


import os
import pathlib

_DATA_FILE = 'day_6.txt'
_CYCLE_SIZE = 7
_NEW_FISH_CYCLE_SIZE = _CYCLE_SIZE + 2


def get_total_lanternfish(fish_data, days, show_daily_growth=False):
    '''
    Function returns total amount of lanternfish after specified number of days.
    '''
    fishes = _CYCLE_SIZE * [0]
    for data in fish_data:
        fishes[data] += 1

    new_fishes = (days + _NEW_FISH_CYCLE_SIZE) * [0]

    for day in range(days):
        fishes[day % _CYCLE_SIZE] += new_fishes[day]
        new_fishes[day + _NEW_FISH_CYCLE_SIZE] = fishes[day % _CYCLE_SIZE]
        if show_daily_growth:
            print(f'Day {day + 1}: {sum(fishes) + sum(new_fishes[day + 1:])}')
    return sum(fishes) + sum(new_fishes[days:])


with open(os.path.join(pathlib.Path(__file__).parent, _DATA_FILE), 'r') as data_file:  # pylint: disable=R1732,W1514 # noqa: E501
    raw_data = data_file.read()

raw_data = [int(fish_data) for fish_data in raw_data.split(',')]

for total_days, show_growth in [(80, True), (256, False)]:
    print(f'Lanternfish population after {total_days} days: {get_total_lanternfish(raw_data, total_days, show_growth)}')
