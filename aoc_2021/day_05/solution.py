from lib.helpers import load_input

import numpy as np

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    point_sets_raw = [row.split(' -> ') for row in data]
    point_sets = []
    for point_set_raw in point_sets_raw:
        points = [[int(y) for y in x.split(',')] for x in point_set_raw]
        point_sets.append(points)

    return np.array(point_sets)

def visit_if_not_diagonal(point_set, grid):
    p0 = point_set[0]
    p1 = point_set[1]
    
    if p0[0] == p1[0]:
        x = p0[0]
        for y in range(min([p0[1], p1[1]]), max([p0[1], p1[1]])+1):
            grid = visit(grid, x,y)
    elif p0[1] == p1[1]:
        y = p0[1]
        for x in range(min([p0[0], p1[0]]), max([p0[0], p1[0]])+1):
            grid = visit(grid, x,y)
    
    return grid

def visit_even_if_diagonal(point_set, grid):
    p0 = point_set[0]
    p1 = point_set[1]
    # print("p0",p0)
    # print("p1",p1)
    
    if p0[0] == p1[0]:
        x = p0[0]
        for y in range(min([p0[1], p1[1]]), max([p0[1], p1[1]])+1):
            grid = visit(grid, x,y)
    elif p0[1] == p1[1]:
        y = p0[1]
        for x in range(min([p0[0], p1[0]]), max([p0[0], p1[0]])+1):
            grid = visit(grid, x,y)
    
    else:
        # print("(p1[1]-p1[1])", (p1[1]-p0[1]))
        # print("(p1[0]-p0[0]", (p1[0]-p0[0]))
        slope = (p1[1]-p0[1])/(p1[0]-p0[0])
        # print("slope",slope)
        # print("min([p0[0], p1[0]])", min([p0[0], p1[0]]))
        # print("max([p0[0], p1[0]])+1)", max([p0[0], p1[0]]))
        num_points = abs(p0[0]-p1[0])
        min_x  = min(p0[0],p1[0])
        for i in range(num_points+1):
            y = min(p0[1], p1[1]) if slope == 1 else max(p0[1],p1[1])
            grid = visit(grid, min_x+i, y+i*slope)

    return grid

def visit(grid, x, y):
    # print("visiting: ",x,y)
    count =grid.get((x,y), 0)
    grid[(x,y)] = count + 1
    return grid

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    
    grid = {}
    for point_set in data:
        grid = visit_if_not_diagonal(point_set, grid)

    overlapping_points = [x for x in grid.keys() if grid.get(x) > 1]
    return len(overlapping_points)

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    
    grid = {}
    for point_set in data:
        grid = visit_even_if_diagonal(point_set, grid)

    overlapping_points = [x for x in grid.keys() if grid.get(x) > 1]
    return len(overlapping_points)

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()