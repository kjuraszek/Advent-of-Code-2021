'''
Advent of Code - Day 16
'''


import os
import pathlib
from functools import reduce


def decode_packet(position):
    '''
    Function recognizes current packet and runs proper decoding function.
    '''
    packet_version, packet_type = get_packet_header(position)
    versions.append(packet_version)
    position += 6
    if packet_type == 4:
        return decode_literal_packet(position)
    length_type_id = get_binary_data(position, position + 1)
    position += 1
    if length_type_id == 0:
        return decode_operator_packet_by_subpackets_length(packet_type, position)
    return decode_operator_packet_by_subpackets_quantity(packet_type, position)


def get_packet_header(position):
    '''
    Function returns packet version and type for current packet.
    '''
    packet_version = get_binary_data(position, position + 3)
    packet_type = get_binary_data(position + 3, position + 6)
    return packet_version, packet_type


def get_binary_data(position_1, position_2):
    '''
    Function returns integer representation of selected binary data.
    '''
    return int(DATA_BINARY[position_1:position_2], 2)


def operation_0(subpackets_values):
    '''
    Function returns sum of subpackets values.
    '''
    return sum(subpackets_values)


def operation_1(subpackets_values):
    '''
    Function returns multiplication of subpackets values.
    '''
    return reduce(lambda a, b: a * b, subpackets_values)


def operation_2(subpackets_values):
    '''
    Function returns minimum value of subpackets values.
    '''
    return min(subpackets_values)


def operation_3(subpackets_values):
    '''
    Function returns maximum value of subpackets values.
    '''
    return max(subpackets_values)


def operation_5(subpackets_values):
    '''
    Function returns 1 if the first value is larger than second.
    Otherwise it returns 0.
    '''
    return 1 if subpackets_values[0] > subpackets_values[1] else 0


def operation_6(subpackets_values):
    '''
    Function returns 1 if the first value is smaller than second.
    Otherwise it returns 0.
    '''
    return 1 if subpackets_values[0] < subpackets_values[1] else 0


def operation_7(subpackets_values):
    '''
    Function returns 1 if both values are equal.
    Otherwise it returns 0.
    '''
    return 1 if subpackets_values[0] == subpackets_values[1] else 0


def decode_literal_packet(position):
    '''
    Function decodes literal packet.
    '''
    end_of_packet = False
    literal_value = ''
    while not end_of_packet:
        group = DATA_BINARY[position:position + 5]
        position += 5
        literal_value += group[1:]
        if group.startswith('0'):
            end_of_packet = True
    literal_value = int(literal_value, 2)
    return (position, literal_value)


def decode_operator_packet_by_subpackets_length(packet_type, position):
    '''
    Function decodes operator packet by subpackets length.
    '''
    total_bits_in_subpackets = get_binary_data(position, position + 15)
    position += 15
    old_position = position
    subpackets_values = []
    while position - old_position < total_bits_in_subpackets:
        position, value = decode_packet(position=position)
        subpackets_values.append(value)
    final_value = calculate_final_value(packet_type, subpackets_values)
    return (position, final_value)


def decode_operator_packet_by_subpackets_quantity(packet_type, position):
    '''
    Function decodes operator packet by subpackets quantity.
    '''
    number_of_subpackets = get_binary_data(position, position + 11)
    position += 11
    subpackets = 0
    subpackets_values = []
    while subpackets < number_of_subpackets:
        position, value = decode_packet(position=position)
        subpackets_values.append(value)
        subpackets += 1
    final_value = calculate_final_value(packet_type, subpackets_values)
    return (position, final_value)


def calculate_final_value(packet_type, subpackets_values):
    '''
    Function returns final value for current operator.
    '''
    return _OPERATIONS[packet_type](subpackets_values)


_DATA_FILE = 'day_16.txt'
_OPERATIONS = {
    0: operation_0,
    1: operation_1,
    2: operation_2,
    3: operation_3,
    5: operation_5,
    6: operation_6,
    7: operation_7
}

with open(os.path.join(pathlib.Path(__file__).parent, _DATA_FILE), 'r') as data_file:  # pylint: disable=W1514
    DATA_RAW = data_file.readline().strip()
    DATA_BINARY = ''.join([f'{int(c, 16):04b}' for c in DATA_RAW])

STARTING_POSITION = 0
versions = []
final_position, packet_value = decode_packet(STARTING_POSITION)


print(f'Sum of versions: {sum(versions)}')
print(f'Final value {packet_value}')
