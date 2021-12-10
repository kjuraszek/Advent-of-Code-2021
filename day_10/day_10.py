'''
Advent of Code - Day 10
'''

import os
import pathlib


_DATA_FILE = 'day_10.txt'
_BRACKETS = {
    '(': {'points': 0, 'matches': ')'},
    ')': {'points': 3, 'matches': '('},
    '[': {'points': 0, 'matches': ']'},
    ']': {'points': 57, 'matches': '['},
    '{': {'points': 0, 'matches': '}'},
    '}': {'points': 1197, 'matches': '{'},
    '<': {'points': 0, 'matches': '>'},
    '>': {'points': 25137, 'matches': '<'},
}

_INCOMPLETE_BRACKETS_VALUES = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4       
}

data = [line.strip() for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                   _DATA_FILE), 'r')]

brackets_sum = 0
incomplete_brackets_sum = []
for row in data:
    stack = []
    for bracket in row:
        if bracket in ['<', '{', '[', '(']:
            stack.append(bracket)
        else:
            prev = stack.pop()
            if prev != _BRACKETS[bracket]['matches']:
                brackets_sum += _BRACKETS[bracket]['points']
                break
    else:
        stack.reverse()
        total_sum = 0
        for incomplete_bracket in stack:
            total_sum *= 5
            total_sum += _INCOMPLETE_BRACKETS_VALUES[incomplete_bracket]
        incomplete_brackets_sum.append(total_sum)

incomplete_brackets_sum.sort()
print(f'Sum of corrupted brackets: {brackets_sum}')
print(f'Middle score of inceomplete bracket: {incomplete_brackets_sum[(len(incomplete_brackets_sum) - 1)//2]}')
