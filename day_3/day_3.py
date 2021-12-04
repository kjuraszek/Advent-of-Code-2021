'''
Advent of Code - Day 3
'''

import os
import pathlib
import collections


_DIAGNOSTIC_FILE = 'day_3.txt'


def get_common_values(diagnostic_data, index):
    '''
    Method to get most and least common values.
    '''
    return collections.Counter([row[index] for row in diagnostic_data]).most_common()


class DiagnosticTool():
    '''
    Diagnostic tool to calculate such parameters as power consumption and life support rating.
    '''
    def __init__(self, data_file) -> None:
        self.diagnostic_data = []
        self.diagnostic_data_width = 0
        self.most_common_bits = []
        self.least_common_bits = []
        self.load_data(data_file)
        self.get_data_width()
        self.get_common_bits()

    def load_data(self, data_file):
        '''
        Method to load the data from a report file.
        '''
        self.diagnostic_data = [line.strip() for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                                           data_file), 'r')]

    def get_data_width(self):
        '''
        Method to calculate data width.
        '''
        self.diagnostic_data_width = len(self.diagnostic_data[0])

    def get_common_bits(self):
        '''
        Method to get least and most common bits.
        '''
        for index in range(self.diagnostic_data_width):
            most_common = get_common_values(self.diagnostic_data, index)
            self.most_common_bits.append(most_common[0][0])
            self.least_common_bits.append(most_common[1][0])

    def get_gamma_rate(self):
        '''
        Method to calculate gamma rate.
        '''
        return int(''.join(self.most_common_bits), 2)

    def get_epsilon_rate(self):
        '''
        Method to calculate epsilon rate.
        '''
        return int(''.join(self.least_common_bits), 2)

    def get_oxygen_generator_rating(self):
        '''
        Method to calculate oxygen generator rating.
        '''
        return int(''.join(self.calculate_rating_by_bit(self.diagnostic_data, 0, self.most_common_bits[0], 'most')), 2)

    def get_co2_scrubber_rating(self):
        '''
        Method to calculate CO2 scrubber rating.
        '''
        return int(''.join(self.calculate_rating_by_bit(self.diagnostic_data, 0, self.least_common_bits[0], 'least')), 2)

    def calculate_rating_by_bit(self, data, position, bit, common):
        '''
        Method to calculate rating by bit.
        '''
        if len(data) == 1:
            return data[0]

        temp_data = []
        most_common_bits = get_common_values(data, position)
        if len(most_common_bits) == 1:
            bit = most_common_bits[0][0]
        else:
            if common == 'most':
                if most_common_bits[0][1] == most_common_bits[1][1]:
                    bit = '1'
                else:
                    bit = most_common_bits[0][0]
            else:
                if most_common_bits[0][1] == most_common_bits[1][1]:
                    bit = '0'
                else:
                    bit = most_common_bits[1][0]

        for row in data:
            if row[position] == bit:
                temp_data.append(row)
        position += 1

        return self.calculate_rating_by_bit(temp_data, position, bit, common)


diagnostic_tool = DiagnosticTool(_DIAGNOSTIC_FILE)

print(f'Power consumption is: {diagnostic_tool.get_gamma_rate() * diagnostic_tool.get_epsilon_rate()}')
print(f'Life support rating is: {diagnostic_tool.get_oxygen_generator_rating() * diagnostic_tool.get_co2_scrubber_rating()}')
