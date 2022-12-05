from lib.helpers import load_input

import numpy as np

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return data

def get_adjacent_indices(i, j, m, n):
    adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data =  np.array([[int(y) for y in list(x)] for x in parse_data(data)])
    m = len(data)
    n = len(data[0])

    low_point_vals = []
    for x in range(m):
        for y in range(n):
            val = data[x][y]
            adj_inds = get_adjacent_indices(x,y,m,n)
            adj_vals = np.array([data[x] for x in adj_inds])
            if (adj_vals > val).all():
                low_point_vals.append(val)
                
    return sum(low_point_vals) + len(low_point_vals)
    
def explore(grid, point):
    visted_points = set()
    visted_points.add(point)
    # print("visted_points", visted_points)

    valid_moves = get_valid_moves(point, grid, visted_points)
    # print("valid_moves", valid_moves)

    while valid_moves:
        for move in valid_moves:
            visted_points.add(move)
        # print("visted_points", visted_points)
        
        valid_moves = sum([get_valid_moves(p, grid, visted_points) for p in visted_points], [])
        # print("valid_moves", valid_moves)

    # print(f"DONE: Visited {len(visted_points)} points in this basin")
    return visted_points

def get_valid_moves(point, grid, visted_points):
    x, y = point[0], point[1]
    m, n = len(grid), len(grid[0])
    possible_moves = get_adjacent_indices(x,y,m,n)
    # print("possible_moves", possible_moves)

    return [move for move in possible_moves  if grid[move] != 9 and move not in visted_points]


def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data =  np.array([[int(y) for y in list(x)] for x in parse_data(data)])
    m = len(data)
    n = len(data[0])

    low_points = []
    for x in range(m):
        for y in range(n):
            val = data[x][y]
            adj_inds = get_adjacent_indices(x,y,m,n)
            adj_vals = np.array([data[x] for x in adj_inds])
            if (adj_vals > val).all():
                low_points.append((x,y))
                
    basins = []
    for p in low_points:
        basin = explore(data, p)
        basins.append(basin)
    
    return np.product(sorted([len(b) for b in basins])[-3:])

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()