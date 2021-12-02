'''
Advent of Code - Day 2
'''

import os
import pathlib


_COMMANDS_FILE = 'day_2.txt'


class SubmarineV1:  # pylint: disable=R0903,C0116
    '''
    First version of the submarine.
    '''
    def __init__(self, command_file) -> None:
        self.commands = []
        self.depth = 0
        self.horizontal_position = 0
        self._load_commands(command_file)
        self._calculate_dimensions()

    def _load_commands(self, command_file) -> None:
        for line in open(os.path.join(pathlib.Path(__file__).parent, command_file), 'r'):  # pylint: disable=R1732,W1514
            cmd_raw = line.strip().split(' ')
            cmd = {
                'command': cmd_raw[0],
                'value': int(cmd_raw[1])
            }
            self.commands.append(cmd)

    def _calculate_dimensions(self) -> None:
        self.horizontal_position = sum([command['value'] for command in self.commands
                                        if command['command'] == 'forward'])
        self.depth = (sum([command['value'] for command in self.commands
                           if command['command'] == 'down'])
                      - sum([command['value'] for command in self.commands
                             if command['command'] == 'up']))

    def calculate_position(self) -> int:
        return self.horizontal_position * self.depth


class SubmarineV2(SubmarineV1):  # pylint: disable=R0903,C0116
    '''
    Second version of the submarine with an updated aim.
    '''
    def __init__(self, command_file) -> None:
        self.aim = 0
        super().__init__(command_file)

    def _calculate_dimensions(self) -> None:
        for command in self.commands:
            if command['command'] == 'forward':
                self.horizontal_position += command['value']
                self.depth += self.aim * command['value']
            elif command['command'] == 'up':
                self.aim -= command['value']
            elif command['command'] == 'down':
                self.aim += command['value']


submarine_v1 = SubmarineV1(_COMMANDS_FILE)
print(submarine_v1.calculate_position())

submarine_v2 = SubmarineV2(_COMMANDS_FILE)
print(submarine_v2.calculate_position())
