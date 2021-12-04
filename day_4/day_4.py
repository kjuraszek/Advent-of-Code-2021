'''
Advent of Code - Day 4
'''

import os
import pathlib

_BINGO_FILE = 'day_4.txt'


def calculate_score(number, board):
    '''
    Method to calculate score based on a winning board.
    '''
    sum_of_numbers = sum([int(num) for index, num in enumerate(board['board']) if not board['state'][index]])
    return int(number) * sum_of_numbers


def mark_number(number, board):
    '''
    Method to check if a number exists and mark it in selected board.
    '''
    if number in board['board']:
        index = board['board'].index(number)
        board['state'][index] = True


class BingoCalculator:
    '''
    Calculator for a bingo game.
    '''
    def __init__(self, boards_file) -> None:
        self.bingo_numbers = []
        self.bingo_boards = []
        self.board_size = 0
        self.load_data(boards_file)

    def load_data(self, boards_file):
        '''
        Method to load the boards data from a file.
        '''
        bingo_data = [line.strip() for line in open(os.path.join(pathlib.Path(__file__).parent,  # pylint: disable=R1732,W1514 # noqa: E501
                                                                 boards_file), 'r')]
        self.bingo_numbers = bingo_data[0].split(',')
        self.board_size = len(bingo_data[2].replace('  ', ' ').split(' '))
        temp_board = []
        for row in bingo_data[2:]:
            if len(row.strip()) > 0:
                temp_board += row.replace('  ', ' ').split(' ')
                if len(temp_board) == self.board_size ** 2:
                    self.bingo_boards.append({
                        'board': temp_board,
                        'state': (self.board_size ** 2) * [False]
                    })
                    temp_board = []

    def run_bingo(self, strategy):
        '''
        Method to simulate a bingo game using two strategies.
        '''
        if strategy == 1:
            for number in self.bingo_numbers:
                for board in self.bingo_boards:
                    mark_number(number, board)
                    if self.check_board(board):
                        print('BINGO')
                        print(f'Winning number: {number}')
                        self.print_board(self.bingo_boards.index(board))
                        print(f'Score: {calculate_score(number, board)}')
                        return
        elif strategy == 2:
            checked_boards = []
            for number in self.bingo_numbers:
                for board in self.bingo_boards:
                    mark_number(number, board)
                    if self.check_board(board) and self.bingo_boards.index(board) not in checked_boards:
                        checked_boards.append(self.bingo_boards.index(board))
                        if len(checked_boards) == len(self.bingo_boards):
                            print('BINGO on the last board')
                            print(f'Winning number: {number}')
                            self.print_board(self.bingo_boards.index(board))
                            print(f'Score: {calculate_score(number, board)}')
                            return

    def check_board(self, board):
        '''
        Method to check if a board is in a winning state.
        '''
        for index in range(self.board_size):
            if all(board['state'][index::self.board_size]):
                return True
        for index in range(0, len(board['state']), self.board_size):
            if all(board['state'][index:index + self.board_size]):
                return True
        return False

    def print_board(self, board_no):
        '''
        Method to print informations about selected board.
        '''
        if board_no not in range(len(self.bingo_boards)):
            return

        print(f'\nBoard no.{board_no + 1} (index: {board_no})\n')
        for index, number in enumerate(self.bingo_boards[board_no]['board']):
            if index % self.board_size == 0:
                board_row = ''
                state_row = ''
            if int(number) < 10:
                number = f' {number}'
            number += ' '
            state = str(self.bingo_boards[board_no]['state'][index])
            if state == 'True':
                state = f' {state}'
            state += ' '
            board_row += number
            state_row += state
            if index % self.board_size == self.board_size - 1:
                print(f'{board_row}\t| {state_row}')


bingo_calculator = BingoCalculator(_BINGO_FILE)
bingo_calculator.run_bingo(strategy=1)
bingo_calculator.run_bingo(strategy=2)
