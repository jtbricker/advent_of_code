from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    points = [tuple(int(x) for x in d.split(',')) for d in data if "fold" not in d]
    folds_raw = [d for d in data if "fold" in d]
    folds = []
    for f in folds_raw:
        tmp = f.split('=')
        folds.append((tmp[0][-1], int(tmp[1]),))
    return points, folds

def flip_point_over_axis(point, axis):
    ax = axis[0]
    ax_val = axis[1]

    if ax == 'x':
        new_y = point[1] #doesn't change
        x = point[0]
        
        assert x != ax_val
        if x < ax_val:
            return point
        
        dx = x - ax_val
        new_x = x - 2*dx

    if ax == 'y':
        new_x = point[0] #doesn't change
        y = point[1]
        
        assert y != ax_val
        if y < ax_val:
            return point
        
        dy = y - ax_val
        new_y = y - 2*dy

    return (new_x, new_y,)

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    points, folds = parse_data(data)
    points = {p:1 for p in points}

    for f in folds[0:1]:
        new_points = {}
        for p in points:
            new_points[flip_point_over_axis(p, f)]=1
        points = new_points
    
    return len(points.keys())

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    points, folds = parse_data(data)
    points = {p:1 for p in points}

    for f in folds:
        new_points = {}
        for p in points:
            new_points[flip_point_over_axis(p, f)]=1
        points = new_points
    
    from matplotlib import pyplot as plt
    xs = [x[0] for x in points.keys()]
    ys = [x[1] for x in points.keys()]
    plt.scatter(xs,ys)
    plt.gca().invert_yaxis()
    plt.show()

    return "Look at the graph"

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()