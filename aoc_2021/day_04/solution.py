from lib.helpers import load_input

import numpy as np

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return data

def is_chosen_number(number, numbers_chosen):
    print(number)
    print(numbers_chosen)
    if number in numbers_chosen:
        return 1
    else:
        return 0

class BingoBoard:
    def __init__(self, board_data, id):
        self.id = id
        self.data = board_data
        self.called = np.zeros(board_data.shape)
    
    def mark_number_and_check(self, number):
        x,y = self._get_loc(number)
        if x is not None and y is not None:
            self.called[x][y] = 1
            return self._is_winner()
        else:
            return False

    def _get_loc(self, number):
        loc = np.where(self.data == number)
        if np.size(loc) > 0:
            return loc[0][0], loc[1][0]
        return None, None
    
    def _is_winner(self):
        column_sums = self.called.sum(axis=0)
        row_sums = self.called.sum(axis=1)
        return np.any(column_sums == 5) or np.any(row_sums == 5)

    def get_uncalled_numbers(self):
        return self.data[np.where(self.called == 0)]
        


def run_bingo_simulation(boards, numbers):
    for number in numbers:
        for board in boards:
            if board.mark_number_and_check(number):
                return board, number

def run_bingo_simulation2(boards, numbers):
    num_boards = len(boards)
    winning_boards = set()

    for number in numbers:
        for board in boards:
            if board.mark_number_and_check(number):
                winning_boards.add(board.id)
                if len(winning_boards) == num_boards:
                    return board, number

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    numbers_chosen = [int(d) for d in data[0].split(',')]

    board_data = data[1:]
    boards = []
    assert len(board_data) % 5 == 0
    for i in range(len(board_data) // 5):
        board = board_data[5*i:5*i+5]
        board = np.array([[int(x) for x in row.split()] for row in board])
        boards.append(BingoBoard(board, id=i))
    
    board, number = run_bingo_simulation(boards, numbers_chosen)

    return board.get_uncalled_numbers().sum() * number

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    numbers_chosen = [int(d) for d in data[0].split(',')]

    board_data = data[1:]
    boards = []
    assert len(board_data) % 5 == 0
    for i in range(len(board_data) // 5):
        board = board_data[5*i:5*i+5]
        board = np.array([[int(x) for x in row.split()] for row in board])
        boards.append(BingoBoard(board, id=i))
    
    board, number = run_bingo_simulation2(boards, numbers_chosen)

    return board.get_uncalled_numbers().sum() * number

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()