'''
A simple script to run script for a specified day

Usage:
day_runner.py --day={NUMBER_OF_DAY_TO_RUN}
'''

import os
import pathlib
import argparse
import importlib


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple script to run script for a specified day.')
    parser.add_argument("--day", type=int, help='Day should be a number in range 1 to 25')
    args = parser.parse_args()
    day = args.day
    if day in range(1, 26):
        project_root = pathlib.Path(__file__).parent
        day_base = f'day_{day}'
        if day_base in os.listdir(project_root):
            print(f'Running script for day {day}')
            day_module_name = f'day_{day}.day_{day}'
            day_module = importlib.import_module(day_module_name)
        else:
            print(f'{day_base} folder doesn\'t exist')
    else:
        raise ValueError('Day should be a number in range 1 to 25')
