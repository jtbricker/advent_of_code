from operator import add, indexOf

from lib.helpers import load_input

import math

instructions = {
    'N': (0,1),
    'S': (0,-1),
    'E': (1,0),
    'W': (-1,0),
}

LEFT = 1
RIGHT = -1

def move(x, y, instr, magnitude):
    dx, dy = instructions.get(instr)
    return x + magnitude*dx, y + magnitude*dy

def turn(cur_ord, direction, degrees):
    ords = ['E','N', 'W', 'S']
    cur_ord_ind = indexOf(ords, cur_ord)
    return ords[(cur_ord_ind + direction*degrees//90)%len(ords)]

def part_1(data):
    """ Return the manhatten distance from the original position (facing east)
    after executing the provided list of instructions. 

    Args:
        data (list[str]): List of instruction for movement of the plane

        Instructions of the form: "{action}{value}", where:
            - Action N means to move north by the given value.
            - Action S means to move south by the given value.
            - Action E means to move east by the given value.
            - Action W means to move west by the given value.
            - Action L means to turn left the given number of degrees.
            - Action R means to turn right the given number of degrees.
            - Action F means to move forward by the given value in the direction the ship is currently facing.

    Returns:
        int: The manhatten distance from the start to the end position
    """

    x = 0
    y = 0
    cur_ord = 'E'

    for d in data:
        instr = d[0]
        mag = int(d[1:])
        if instr == 'L':
            cur_ord = turn(cur_ord, LEFT, degrees=mag)
            continue
        if instr == 'R':
            cur_ord = turn(cur_ord, RIGHT, degrees=mag)
            continue
        elif instr == 'F':
            instr = cur_ord
        
        x, y = move(x, y, instr, mag)

    return abs(x) + abs(y)


class Waypoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def turn(self, dir, degrees):
        rads = dir * math.radians(degrees)
        x_rot = int(round(self.x*math.cos(rads) - self.y*math.sin(rads)))
        y_rot = int(round(self.x*math.sin(rads) + self.y*math.cos(rads)))

        self.x = x_rot
        self.y = y_rot

    def move(self, instr, magnitude):
        dx, dy = instructions.get(instr)
        self.x += magnitude*dx
        self.y += magnitude*dy

class Ship:
    def __init__(self, waypoint):
        self.x = 0
        self.y = 0
        self.waypoint = waypoint

    def move(self, magnitude):
        # Move in the direction of the waypoint "magnitude" times
        self.x += magnitude*self.waypoint.x
        self.y += magnitude*self.waypoint.y
    
    def instruct(self, instruction, magnitude):
        if instruction == 'L':
            self.waypoint.turn(LEFT, magnitude)
        elif instruction == 'R':
            self.waypoint.turn(RIGHT, magnitude)
        elif instruction == 'F':
            self.move(magnitude)
        else:
            self.waypoint.move(instruction, magnitude)
        


def part_2(data):
    """ Return the manhatten distance from the original position (facing east)
    after executing the provided list of instructions. 

    Args:
        data (list[str]): List of instruction for movement of the plane

        Instructions of the form: "{action}{value}", where:
            - Action N means to move the waypoint north by the given value.
            - Action S means to move the waypoint south by the given value.
            - Action E means to move the waypoint east by the given value.
            - Action W means to move the waypoint west by the given value.
            - Action L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
            - Action R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
            - Action F means to move forward to the waypoint a number of times equal to the given value.

    Returns:
        int: The manhatten distance from the start to the end position
    """
    waypoint = Waypoint(10, 1) # Starts 10 units east and 1 unit north
    ship = Ship(waypoint)

    for d in data:
        instr = d[0]
        mag = int(d[1:])
        ship.instruct(instr, mag)

    return abs(ship.x) + abs(ship.y)

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()