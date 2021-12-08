'''
Advent of Code - Day 8
'''

import os
import pathlib


_DATA_FILE = 'day_8.txt'
_UNIQUE_DIGITS = {
    2: '1',
    3: '7',
    4: '4',
    7: '8'
}
_NON_UNIQUE_DIGITS_SEGMENTS = {
    0: ['top', 'top-left', 'top-right', 'bottom-left', 'bottom-right', 'bottom'],
    2: ['top', 'top-right', 'middle', 'bottom-left', 'bottom'],
    3: ['top', 'top-right', 'middle', 'bottom-right', 'bottom'],
    5: ['top', 'top-left', 'middle', 'bottom-right', 'bottom'],
    6: ['top', 'top-left', 'middle', 'bottom-left', 'bottom-right', 'bottom'],
    9: ['top', 'top-left', 'top-right', 'middle', 'bottom-right', 'bottom']
}


def generate_non_unique_digits_connections(used_connections: dict[str, set]) -> dict[int, set]:
    '''
    Function returns a connections between segments and each non unique digit.
    '''
    connected_digits = {}
    for digit, segment in _NON_UNIQUE_DIGITS_SEGMENTS.items():
        connected_digits[digit] = {connection.copy().pop() for key, connection in used_connections.items() if key in segment}
    return connected_digits


raw_data = [line.strip().split(' | ') for line in open(os.path.join(pathlib.Path(__file__).parent, _DATA_FILE), 'r')]  # pylint: disable=R1732,W1514 # noqa: E501

digits_patterns = [data[0] for data in raw_data]
digit_values = [data[1] for data in raw_data]

DIGITS_1478_APPEARANCE = 0
TOTAL_SUM = 0
for index, _ in enumerate(digits_patterns):
    pattern = digits_patterns[index].split(' ')
    connections = {
        'top': set(),
        'top-left': set(),
        'top-right': set(),
        'middle': set(),
        'bottom-left': set(),
        'bottom-right': set(),
        'bottom': set()
    }
    digit_1 = [letters for letters in pattern if len(letters) == 2].pop()
    digit_4 = [letters for letters in pattern if len(letters) == 4].pop()
    digit_7 = [letters for letters in pattern if len(letters) == 3].pop()
    digit_8 = [letters for letters in pattern if len(letters) == 7].pop()

    connections['top'] = set(digit_7) - set(digit_1)

    length_6_digits = [letters for letters in pattern if len(letters) == 6]
    length_5_digits = [letters for letters in pattern if len(letters) == 5]

    digit_6 = [letters for letters in length_6_digits if not all([digit in letters for digit in digit_7])].pop()
    length_6_digits.pop(length_6_digits.index(digit_6))

    connections['top-right'] = set(digit_8) - set(digit_6)

    digit_9 = [letters for letters in length_6_digits if all([digit in letters for digit in digit_4])].pop()
    length_6_digits.pop(length_6_digits.index(digit_9))

    connections['bottom-left'] = set(digit_8) - set(digit_9)

    digit_0 = length_6_digits.pop()

    connections['middle'] = set(digit_8) - set(digit_0)
    connections['bottom-right'] = set(digit_1) - connections['top-right']

    digit_3 = [letters for letters in length_5_digits if all([digit in letters for digit in digit_7])].pop()
    length_5_digits.pop(length_5_digits.index(digit_3))

    connections['top-left'] = set(digit_9) - set(digit_3) - connections['bottom-left']
    connections['bottom'] = set(digit_8) - {c.copy().pop() for c in connections.values() if len(c) > 0}

    non_unique_digits_connections = generate_non_unique_digits_connections(connections)
    OUTPUT_VALUE = ''
    for value in digit_values[index].split(' '):
        if len(value) in _UNIQUE_DIGITS:
            OUTPUT_VALUE += _UNIQUE_DIGITS[len(value)]
            DIGITS_1478_APPEARANCE += 1
        elif len(value) == 6 or len(value) == 5:
            for d in [0, 6, 9, 2, 3, 5]:
                if set(value) == non_unique_digits_connections[d]:
                    OUTPUT_VALUE += str(d)
                    break
    print(f'Row {index + 1}: {raw_data[index]} -> {OUTPUT_VALUE}')
    TOTAL_SUM += int(OUTPUT_VALUE)

print(f'Digits [1, 4, 7, 8] appearance: {DIGITS_1478_APPEARANCE}')
print(f'Total sum of decoded digits: {TOTAL_SUM}')
