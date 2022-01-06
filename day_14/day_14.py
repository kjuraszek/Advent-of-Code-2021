'''
Advent of Code - Day 14
'''

import os
import pathlib
import collections


def add_new_pair(pair_tuple, current_pairs):
    '''
    Function adds a pair and its number to a current pairs dict
    '''
    if pair_tuple[0] not in current_pairs:
        current_pairs[pair_tuple[0]] = 0
    current_pairs[pair_tuple[0]] += pair_tuple[1]


_DATA_FILE = 'day_14.txt'
_STEPS_TO_CHECK = [40, 10]
_MAXIMUM_STEPS = max(_STEPS_TO_CHECK)

data = [line.strip() for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                   _DATA_FILE), 'r')]

with open(os.path.join(pathlib.Path(__file__).parent, _DATA_FILE), 'r') as data_file:  # pylint: disable=W1514
    TEMPLATE = data_file.readline().strip()
    INSTRUCTIONS_RAW = data_file.read().strip().split('\n')
    INSTRUCTIONS = {element.split(' -> ')[0]: element.split(' -> ')[1] for element in INSTRUCTIONS_RAW}

pairs_raw = [TEMPLATE[index] + TEMPLATE[index + 1] for index, _ in enumerate(TEMPLATE) if index < len(TEMPLATE) - 1]
pairs = collections.Counter(pairs_raw).most_common()
letters = set(''.join([pair[0] for pair in pairs]))
polymer_counter = {letter: 0 for letter in letters}

for step in range(_MAXIMUM_STEPS):
    new_pairs = {}
    for pair in pairs:
        if pair[0] in INSTRUCTIONS:
            new_polymer = INSTRUCTIONS[pair[0]]
            new_pair_1 = pair[0][0] + new_polymer
            new_pair_2 = new_polymer + pair[0][1]
            if new_polymer not in polymer_counter:
                polymer_counter[new_polymer] = 0
            polymer_counter[new_polymer] += pair[1]
            add_new_pair((new_pair_1, pair[1]), new_pairs)
            add_new_pair((new_pair_2, pair[1]), new_pairs)
        else:
            add_new_pair(pair, new_pairs)
    pairs = collections.Counter(new_pairs).most_common()
    if step + 1 in _STEPS_TO_CHECK:
        sorted_polymers = sorted(polymer_counter.values())
        print(f'Step: {step + 1}, polymer subtraction: {sorted_polymers[-1] - sorted_polymers[0]}')
