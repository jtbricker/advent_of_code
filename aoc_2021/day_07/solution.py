from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return [int(x) for x in data[0].split(',')]

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    min_pos = min(data)
    max_pos = max(data)

    print(min_pos, max_pos)

    fuels = []
    for i in range(min_pos, max_pos+1):
        fuel = 0
        for d in data:
            fuel += abs(d-i)
        fuels.append(fuel)
    
    return min(fuels)

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    min_pos = min(data)
    max_pos = max(data)

    # print(min_pos, max_pos)

    fuels = []
    for i in range(min_pos, max_pos+1):
        fuel = 0
        for d in data:
            n = abs(d-i)
            fuel += n * (n + 1) // 2
            # print(n, fuel)
        fuels.append(fuel)
    
    return min(fuels)

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()