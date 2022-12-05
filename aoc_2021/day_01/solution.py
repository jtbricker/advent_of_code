from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return [int(x) for x in data]

def count_rolling_increases(data, window):
    count = 0
    for i in range(0,len(data)-window):
        if sum(data[i+1:i+window+1]) > sum(data[i:i+window]):
            count += 1
    return count

def part_1(data):
    """ Given a list of integers, return the number of times a number in
    the list is larger than the previous number (ignoring the first number)

    Args:
        data (List<int>): List of ocean depths

    Returns:
        int: Number of times the depth increased
    """
    data = parse_data(data)
    return count_rolling_increases(data, window=1)

def part_2(data):
    """ Given a set of integers, run a window along the list and take the sum.
    Return the number of times this sum increased from the previous sum (ignoring the first window)

    Args:
        data (List<int>): List of ocean depths

    Returns:
        int: Number of times the sum of a running window of 3 depth measures increased
    """
    data = parse_data(data)
    
    return count_rolling_increases(data, window=3)

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()