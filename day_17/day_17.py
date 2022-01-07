'''
Advent of Code - Day 17
'''


import os
import pathlib


def calculate_min_velocity_x():
    '''
    Function calculates a minimum x velocity needed to approach the target area.
    '''
    sum_steps = 0
    step = 0
    while sum_steps < abs(MIN_X):
        step += 1
        sum_steps += step
    return step if MIN_X > 0 else step * -1


def test_velocity(velocity_x, velocity_y):
    '''
    Function tests pair of the velocities if they allow to reach the target area in any step.
    If they approach the target area a maximum height is returned.
    Otherwise this function returns None.
    '''
    current_x = current_y = 0
    highest_y = 0
    while current_y >= MIN_Y and current_x <= MAX_X:
        current_x += velocity_x
        if velocity_x > 0:
            velocity_x -= 1
        elif velocity_x < 0:
            velocity_x += 1
        current_y += velocity_y
        velocity_y -= 1
        if current_y > highest_y:
            highest_y = current_y
        if MIN_Y <= current_y <= MAX_Y and MIN_X <= current_x <= MAX_X:
            return highest_y
    return None


_DATA_FILE = 'day_17.txt'

with open(os.path.join(pathlib.Path(__file__).parent, _DATA_FILE), 'r') as data_file:  # pylint: disable=W1514
    DATA_RAW = data_file.readline().strip().replace('target area: ', '').replace(' ', '').split(',')
    MIN_X, MAX_X = sorted([int(value) for value in DATA_RAW[0].replace('x=', '').split('..')])
    MIN_Y, MAX_Y = sorted([int(value) for value in DATA_RAW[1].replace('y=', '').split('..')])


MIN_VELOCITY_X = calculate_min_velocity_x()
MAX_VELOCITY_X = MAX_X
HIGHEST_POSITIONS = []

for starting_x in range(MIN_VELOCITY_X, MAX_VELOCITY_X + 1):
    for starting_y in range(MIN_Y, abs(MIN_Y)):
        calculation = test_velocity(starting_x, starting_y)
        if calculation is not None:
            HIGHEST_POSITIONS.append(calculation)

HIGHEST_POSITIONS.sort()
print(f'Highest position: {HIGHEST_POSITIONS[-1]}')
print(f'Total initial velocities: {len(HIGHEST_POSITIONS)}')
