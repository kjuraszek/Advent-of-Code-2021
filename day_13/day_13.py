'''
Advent of Code - Day 13
'''


import os
import pathlib


_DATA_FILE = 'day_13.txt'

with open(os.path.join(pathlib.Path(__file__).parent, _DATA_FILE), 'r') as data_file:
    DATA_RAW = data_file.read().strip().split('\n\n')
    LIST_OF_DOTS = [(position.split(',')) for position in DATA_RAW[0].split('\n')]
    LIST_OF_DOTS = [tuple([int(position[0]), int(position[1])]) for position in LIST_OF_DOTS]
    
    INSTRUCTIONS = [instruction.replace('fold along ', '').split('=') for instruction in DATA_RAW[1].split('\n')]
    INSTRUCTIONS = [tuple([instruction[0], int(instruction[1])]) for instruction in INSTRUCTIONS]


MAX_X = max([position[0] for position in LIST_OF_DOTS])
MAX_Y = max([position[1] for position in LIST_OF_DOTS])

paper = [[0] * (MAX_X + 1) for _ in range(MAX_Y + 1)]

for dot_x, dot_y in LIST_OF_DOTS:
    paper[dot_y][dot_x] = 1
    

for instruction, value in INSTRUCTIONS:
    if instruction == 'x':
        for index_y, row in enumerate(paper):
            for index_x, cell in enumerate(row):
                if index_x > value and cell == 1:
                    index_x_after_fold = value - abs(index_x - value)
                    paper[index_y][index_x_after_fold] = 1
            paper[index_y] = row[:value]
    elif instruction == 'y':
        for index_y, row in enumerate(paper):
            for index_x, cell in enumerate(row):
                if index_y > value and cell == 1:
                    index_y_after_fold = value - abs(index_y - value)
                    paper[index_y_after_fold][index_x] = 1
        paper = paper[:value]

    sum_of_dots = sum([sum(row) for row in paper])
    print(f'Sum of dots for this step: {sum_of_dots}')



for line in paper:
    print(line)
print('The code is CPZLPFZL')  # TODO: make it cleaner