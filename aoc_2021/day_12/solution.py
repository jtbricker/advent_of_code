from os import dup
from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    connects = {'dead_end': [], 'end':[]}
    for line in data:
        [x,y]=line.split('-')
        if y == 'start' or x == 'end':
            x,y = y,x
        existing = connects.get(x, [])
        connects[x] = existing + [y]
        if x != 'start' and y != 'end':
            existing = connects.get(y, [])
            connects[y] = existing + [x]
    return connects

def explore(caves, paths):
    new_paths = []
    for path in paths:
        nexts = caves[path[-1]]
        
        if len(nexts) == 0:
            new_paths.append(path)
            continue

        for next in nexts:
            new_path = path.copy()
            if next.lower() == next and next not in path:
                new_path += [next]
            elif next.upper() == next:
                new_path += [next]
            else:
                new_path += ['dead_end']
            new_paths.append(new_path)
    if len(new_paths) == 0:
        return paths
    return new_paths

def explore_v2(caves, paths):
    new_paths = []
    for path in paths:
        nexts = caves[path[-1]]
        
        if len(nexts) == 0:
            new_paths.append(path)
            continue

        for next in nexts:
            new_path = path.copy()
            if next.lower() == next and (next not in path or not small_cave_visited_twice(path)):
                new_path += [next]
            elif next.upper() == next:
                new_path += [next]
            else:
                new_path += ['dead_end']
            new_paths.append(new_path)
    if len(new_paths) == 0:
        return paths
    return new_paths

def small_cave_visited_twice(path):
    seen = set()
    dupes = [x for x in path if x == x.lower() and x in seen or seen.add(x)]
    assert len(dupes) <= 1
    return len(dupes) == 1

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    caves = parse_data(data)

    paths = [["start"]]

    last_length = 0
    while True:
        paths = explore(caves, paths)
        path_length = len([p for p in paths if p[-1] != 'dead_end'])
        if path_length == last_length:
            break
    
        last_length = path_length
    
    return path_length

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    caves = parse_data(data)

    paths = [["start"]]

    last_length = 0
    while True:
        paths = explore_v2(caves, paths)
        path_length = len([p for p in paths if p[-1] != 'dead_end'])
        if path_length == last_length:
            break
    
        last_length = path_length
    
    return path_length

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()