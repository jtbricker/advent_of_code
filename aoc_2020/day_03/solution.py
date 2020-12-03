from lib.helpers import load_input

def count_trees_on_slope(data, x_slope, y_slope):
    x = 0
    y = 0
    tree_count = 0
    for _ in range(0, len(data)-y_slope, y_slope):
        x += x_slope
        y += y_slope
        x_acc = x % len(data[y])
        if data[y][x_acc] == '#':
            tree_count += 1

    return tree_count

def part_1(data):
    """Count the number of trees encountered when starting at the top-left of
    the map and moving right 3, down 1.

    Args:
        data ([list of strings]): Each row is a fixed column string where "." 
        represent open spaces in a map and "#" represent trees
    """

    return count_trees_on_slope(data, 3, 1)
    

def part_2(data):
    """Count the number of trees encountered when starting at the top-left of
    the map and moving at various slopes, multiply the counts together.

    Args:
        data ([list of strings]): Each row is a fixed column string where "." 
        represent open spaces in a map and "#" represent trees
    """
    return ( 
        count_trees_on_slope(data, 1, 1) *
        count_trees_on_slope(data, 3, 1) *
        count_trees_on_slope(data, 5, 1) *
        count_trees_on_slope(data, 7, 1) *
        count_trees_on_slope(data, 1, 2) 
    )


def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()