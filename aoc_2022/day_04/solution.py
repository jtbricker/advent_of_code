from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    pairs = []
    for pair in data:
        assignment_1, assignment_2 = pair.split(',')
        start1, end1 = [int(x) for x in assignment_1.split('-')]
        start2, end2 = [int(x) for x in assignment_2.split('-')]
        pairs.append((range(start1, end1+1), range(start2, end2+1)))

    return pairs

def is_contained(range1, range2):
    set1 = set(range1)
    set2 = set(range2)
    return set1 == set1.intersection(set2)

def are_intersecting(range1, range2):
    set1 = set(range1)
    set2 = set(range2)
    return len(set1.intersection(set2)) > 0

def part_1(data):
    """ Given a list of paired ranges, return the count of pairs in which
    one of the ranges completely encompasses the other

    e.g. 2-8,3-7 . (the second range is completed contained within the first)

    Args:
        data (List(str)]): The pair of range in the format: start1-end1,start2-end2

    Returns:
        [int]: The number of pairs in which one ranges contains the other completely
    """
    pairs = parse_data(data)

    count = 0
    for pair in pairs:
        if is_contained(pair[0], pair[1]) or is_contained(pair[1], pair[0]):
            count += 1
    
    return count

def part_2(data):
    """ Given a list of paired ranges, return the count of pairs in which
    the ranges intersect at all

    e.g. 2-8,7-9 . (the ranges shared 7-8)

    Args:
        data (List(str)]): The pair of range in the format: start1-end1,start2-end2

    Returns:
        [int]: The number of pairs in which the ranges intersect
    """
    pairs = parse_data(data)

    count = 0
    for pair in pairs:
        if are_intersecting(pair[0], pair[1]):
            count += 1
    
    return count

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()