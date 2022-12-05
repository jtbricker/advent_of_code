from copy import deepcopy

from lib.helpers import load_input


def are_adjacent_seats_occupied(seats, x, y, max_count):
    occupied_count = 0
    for i in range(max(0, x-1), min(x+2, len(seats))):
        for j in range(max(0, y-1), min(y+2, len(seats[0]))):
            if i == x and j == y:
                continue

            if seats[i][j] == '#':
                occupied_count += 1
    
    return occupied_count <= max_count

def check_visual_direction_occupied(seats, x, y, dx, dy):
    i = x + dx
    j = y + dy


    while i >=0 and j>=0:
        try:
            if seats[i][j] == '#':
                return True
            if seats[i][j] == 'L':
                return False
        except IndexError:
            return False
        i += dx
        j += dy
    
    return False

def are_visually_adjacent_seats_occupied(seats, x, y, max_count):   
    occupied_count = 0

    directions = [
        (0,1, "RIGHT"), 
        (0,-1, "LEFT"), 
        (1,0, "DOWN"), 
        (-1,0, "UP"), 
        (1,1, "DOWN/RIGHT"), 
        (-1,-1, "UP/LEFT"), 
        (1,-1, "DOWN/LEFT"), 
        (-1,1, "UP/RIGHT")
    ]
    
    for dx, dy, _dir in directions:
        if check_visual_direction_occupied(seats, x, y, dx, dy):
            occupied_count += 1

        if occupied_count > max_count:
            return True

    return False

def part_1(data):
    """ Determine the number of occupied seats after seats reach an equilibrium by the follow rules

        - If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
        - If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
        - Otherwise, the seat's state does not change.


    Args:
        data (list[str]): List of strings representing a seating map where L is an empty seat, # is 
        an occupied seat, and . is the floor.

    Returns:
        [int]: Number of occupied seats after an equilibrium is reached
    """
    seats_before = deepcopy(data)
    num_occupied = 0
    num_changes = None
    while num_changes is None or num_changes > 0:
        num_changes = 0
        seats_after = deepcopy(seats_before)
        for x in range(len(seats_before)):
            for y in range(len(seats_before[0])):
                if seats_before[x][y] == 'L' and are_adjacent_seats_occupied(seats_before, x,y, max_count=0):
                    seats_after[x][y] = '#'
                    num_changes += 1
                    num_occupied += 1
                elif seats_before[x][y] == '#' and not are_adjacent_seats_occupied(seats_before, x, y, max_count=3):
                    seats_after[x][y] = 'L'
                    num_changes += 1
                    num_occupied -= 1
        seats_before = seats_after
                

    return num_occupied

def part_2(data):
    """ Determine the number of occupied seats after seats reach an equilibrium by the follow rules

        - If a seat is empty (L) and there are no occupied seats visually adjacent to it, the seat becomes occupied.
        - If a seat is occupied (#) and five or more seats visually adjacent to it are also occupied, the seat becomes empty.
        - Otherwise, the seat's state does not change.


    Args:
        data (list[str]): List of strings representing a seating map where L is an empty seat, # is 
        an occupied seat, and . is the floor.

    Returns:
        [int]: Number of occupied seats after an equilibrium is reached
    """
    seats_before = deepcopy(data)
    num_occupied = 0
    num_changes = None
    while num_changes is None or num_changes > 0:
        num_changes = 0
        seats_after = deepcopy(seats_before)
        
        for x in range(len(seats_before)):
            for y in range(len(seats_before[0])):
                if seats_before[x][y] == 'L' and not are_visually_adjacent_seats_occupied(seats_before, x,y, max_count=0):
                    seats_after[x][y] = '#'
                    num_changes += 1
                    num_occupied += 1
                elif seats_before[x][y] == '#' and are_visually_adjacent_seats_occupied(seats_before, x, y, max_count=4):
                    seats_after[x][y] = 'L'
                    num_changes += 1
                    num_occupied -= 1
        seats_before = seats_after

    return num_occupied


def main():
    data = [[c for c in line] for line in load_input(__file__, 'input.txt')]

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()