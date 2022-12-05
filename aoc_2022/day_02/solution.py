from lib.helpers import load_input

def parse_data(data):
    moves = []
    for game in data:
        their_move, my_move = game.split()
        moves.append({'their_move': move_dict[their_move], 'my_move':move_dict[my_move]})

    return moves

def parse_data2(data):
    moves = []
    for game in data:
        their_move, my_move = game.split()
        moves.append({'their_move': move_dict[their_move], 'my_move':input_dict2[(their_move, my_move)]})

    return moves

move_dict = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

input_dict2 = {
    ('A', 'X'): 'scissors',
    ('A', 'Y'): 'rock',
    ('A', 'Z'): 'paper',
    ('B', 'X'): 'rock',
    ('B', 'Y'): 'paper',
    ('B', 'Z'): 'scissors',
    ('C', 'X'): 'paper',
    ('C', 'Y'): 'scissors',
    ('C', 'Z'): 'rock',
}

points_dict = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}

def play_game(their_move, my_move):
    points = 0
    
    # Game is tied
    if their_move == my_move:
        # print("Tied!\t", "their move: ", their_move, "\t\tmy move: ", my_move)
        return points + 3

    # I win
    if (
        their_move == 'rock' and my_move == 'paper' or
        their_move == 'paper' and my_move == 'scissors' or
        their_move == 'scissors' and my_move == 'rock'
    ):
        # print("I win!\t", "their move: ", their_move, "\t\tmy move: ", my_move)
        return points + 6
    
    # print("I lose!\t", "their move: ", their_move, "\t\tmy move: ", my_move)
    return points

def part_1(data):
    """Determine the points you will receive from a rock, paper, scissors tournament
    given the following:

    1. Each game is represented by a row in the input
    2. The first column of each row represents your opponent's move (A=rock, B=paper, C=scissors)
    3. The second column  of each row represents your move (X=rock, Y=paper, Z=scissors)
    4. Your score for a game is dependent on whether your win (0 for loss, 3 for tie, 6 for win) and
        what symbol you chose (1 for rock, 2 for paper, 3 for scissors)
    5. Your total score is the sum of the scores from each round

    Args:
        data (List[str]): Each string in the list contains two characters which represent your opponent's and your move

    Returns:
        int: The total score across all games
    """
    data = parse_data(data)

    total_score = 0
    for d in data:
        total_score += points_dict[d['my_move']] + play_game(d['their_move'], d['my_move'])
    return total_score

def part_2(data):
    """Determine the points you will receive from a rock, paper, scissors tournament
    given the following:

    1. Each game is represented by a row in the input
    2. The first column of each row represents your opponent's move (A=rock, B=paper, C=scissors)
    3. The second column of each row represents the intended outcome (X=lose, Y=draw, Z=win)
    4. Your score for a game is dependent on whether your win (0 for loss, 3 for tie, 6 for win) and
        what symbol you chose (1 for rock, 2 for paper, 3 for scissors)
    5. Your total score is the sum of the scores from each round

    Args:
        data (List[str]): Each string in the list contains two characters which represent your opponent's and your move

    Returns:
        int: The total score across all games
    """
    data = parse_data2(data)

    total_score = 0
    for d in data:
        total_score += points_dict[d['my_move']] + play_game(d['their_move'], d['my_move'])
    return total_score

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()