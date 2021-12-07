'''
A simple script to prepare files for a specified day

Usage:
day_generator.py --day={NUMBER_OF_DAY_TO_CREATE}
'''

import os
import pathlib
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='A simple script to generate data for a specified day.')
    parser.add_argument("--day", type=int, help='Day should be a positive number')
    args = parser.parse_args()
    day = args.day
    if day > 0:
        project_root = pathlib.Path(__file__).parent
        day_base = f'day_{day}'
        day_root = os.path.join(pathlib.Path(__file__).parent, day_base)
        if day_base not in os.listdir(project_root):
            # pylint: disable=W1514
            os.mkdir(day_root)
            with open(os.path.join(day_root, '__init__.py'), 'w') as day_file:
                pass
            with open(os.path.join(day_root, f'{day_base}.txt'), 'w') as day_file:
                pass
            with open(os.path.join(day_root, f'{day_base}.py'), 'w') as day_file:
                string_to_write = f"'''\nAdvent of Code - Day {day}\n'''\n\n"
                day_file.write(string_to_write)
            print(f'Created files for a {day_base}')
        else:
            print(f'{day_base} folder already exists')

    else:
        raise ValueError('Day should be a positive number')
