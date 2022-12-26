from lib.helpers import load_input
import numpy as np

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    data_parsed = []
    for d in data:
        row = []
        for i in d:
            row.append(int(i))
        data_parsed.append(row)
    return np.array(data_parsed)

def count_visible_interior_trees(data):
    visible_count = 0
    for i in range(1, len(data)-1):
        for j in range(1, len(data[0])-1):
            tree_height = data[i,j]

            left = data[i, 0:j]
            right = data[i, j+1:]
            up = data[0:i, j]
            down = data[i+1:, j]

            if np.all(left < tree_height) or \
                np.all(right < tree_height) or \
                np.all(up < tree_height) or \
                np.all(down < tree_height):
                
                visible_count += 1
    return visible_count           

def part_1(data):
    """ Given a grid of number that represent heights of trees
    determine the number of trees that can be seen from any side
    outside of the grid.

    A tree can be seen from outside the grid if it is on the edge of the grid 
    or if there is any tree horizontally or vertically that has a smaller height

    Args:
        data ( array<array<int>>): A grid of integers representing tree heights 

    Returns:
        int: The number of trees that can be seen from outside the grid
    """
    data = parse_data(data)

    num_rows = len(data)
    num_cols = len(data[0])
    outside_trees = 2*num_rows + 2*num_cols - 4
    
    inside_visible_trees = count_visible_interior_trees(data)

    return outside_trees + inside_visible_trees

def calculate_direction_score(arr, height, reverse=False):
    if reverse:
        arr = np.flip(arr)
    
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] >= height:
            return count
    return count

def calculate_scenic_score(data, i, j):
    tree_height = data[i,j]
    left = data[i, 0:j]
    right = data[i, j+1:]
    up = data[0:i, j]
    down = data[i+1:, j]
    
    left_score = calculate_direction_score(left, tree_height, reverse=True)
    right_score = calculate_direction_score(right, tree_height)
    up_score = calculate_direction_score(up, tree_height, reverse=True)
    down_score = calculate_direction_score(down, tree_height)

    scenic_score = left_score * right_score * up_score * down_score

    return scenic_score

def part_2(data):
    """ Given a grid of number that represent heights of trees
    determine the maximum "scenic score", defined as the product 
    of the number of trees that can be seen in all 4 directions
    from a given "tree of interest" (TOI)

    A tree can be seen from a TOI if all trees between it and the TOI
    are shorter than the TOI

    Args:
        data ( array<array<int>>): A grid of integers representing tree heights 

    Returns:
        int: The maxmimum scenic score of the forrest
    """
    data = parse_data(data)
    
    scores = []
    for i in range(1, len(data) - 1):
        for j in range(1, len(data[0]) - 1):
            scores.append(calculate_scenic_score(data, i, j))
    return max(scores)

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()