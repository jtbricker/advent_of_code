from lib.helpers import load_input_chunked

def parse_data(data):
    return data

def part_1(data):
    """ Given a list of groups of integers, find the 
    sum of integers in the group with the highest sum

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    
    max_sum = 0
    for d in data:
        cals = [int(x) for x in d]
        cals_sum = sum(cals)
        if cals_sum > max_sum:
            max_sum = cals_sum
    return max_sum

def part_2(data):
    """Given a list of groups of integers, find the 
    sum of three groups with the highest sums

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    sums = []
    for d in data:
        cals = [int(x) for x in d]
        cals_sum = sum(cals)
        sums.append(cals_sum)
    return sum(sorted(sums, reverse=True)[:3])
    
    

def main():
    data = load_input_chunked(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()