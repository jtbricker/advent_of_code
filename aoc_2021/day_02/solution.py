from lib.helpers import load_input

moves = {
    'forward': (1,0),
    'down': (0,1),
    'up': (0,-1)
}

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    data = [x.split() for x in data]
    return [[x[0],int(x[1])] for x in data]

def part_1(data):
    """ Given a list of instructions of the form "<direction> <magnitude>"
    and starting from horizontal_pos and depth of 0,0.  Determine
    the (final depth * horizontal_pos) based on the following rules:

        * "forward X" => increases the horizontal position by X units.
        * "down X" => increases the depth by X units.
        * "up X" => decreases the depth by X units.

    Args:
        data (List[List[string, int]]): List of directions

    Returns:
        int: final depth*horizontal_pos
    """
    data = parse_data(data)

    horiz = 0
    depth = 0
    for move in data:
        dir = move[0]
        mag = move[1]

        v_x, v_y = moves[dir]

        if horiz + v_x*mag >= 0:
            horiz += v_x*mag

        if depth + v_y*mag >= 0:
            depth += v_y*mag 

    return horiz*depth


def part_2(data):
    """Given a list of instructions of the form "<direction> <magnitude>"
    and starting from horizontal_pos and depth of 0,0.  Determine
    the (final depth * horizontal_pos) based on the following rules:

        * "down X": increases your aim by X units.
        * "up X": decreases your aim by X units.
        * "forward X": does two things:
            * It increases your horizontal position by X units.
            * It increases your depth by your aim multiplied by X.

    Args:
        data (List[List[string, int]]): List of directions

    Returns:
        int: final depth*horizontal_pos
    """
    data = parse_data(data)

    horiz = 0
    depth = 0
    aim = 0
    for move in data:
        dir = move[0]
        mag = move[1]

        if dir == 'down' and aim + mag >= 0:
            aim += mag

        elif dir == 'up' and aim - mag >= 0:
            aim -= mag

        elif dir == 'forward':
            horiz += mag
            depth += mag*aim
        
    return horiz*depth

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()