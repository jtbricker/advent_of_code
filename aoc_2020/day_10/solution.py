from lib.helpers import load_input

def part_1(data):
    """ What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?

    Args:
        data (list[int]): List of adapter output ratings (in jolts)
    """
    # The outlet as a rating of 0
    # The device has a rating equal to the max adapter rating + 3
    jolt_ratings = [0] + sorted(data) + [max(data)+3]
    num_one_diff = 0
    num_three_diff = 0
    for i in range(len(jolt_ratings)-1):
        diff = jolt_ratings[i+1] - jolt_ratings[i]
        if  diff == 1:
            num_one_diff += 1
        elif diff == 3:
            num_three_diff += 1

    return num_one_diff*num_three_diff

memo_count_possible_combinations = {}
def count_possible_combinations(adapters):
    if len(adapters) in memo_count_possible_combinations:
        return memo_count_possible_combinations[len(adapters)]
    if len(adapters) <= 1:
        return 1
    i = 1
    count = 0
    diff = adapters[i] - adapters[0]
    
    while diff <= 3:
        count += count_possible_combinations(adapters[i:])
        i += 1
        if i >= len(adapters):
            break
        diff = adapters[i] - adapters[0]

    memo_count_possible_combinations[len(adapters)] = count
    return count


def part_2(data):
    """ Count the number of unique possible adapter configurations given

    Args:
        data (list[int]): List of adapter output ratings (in jolts)
    """
    # The outlet as a rating of 0
    # The device has a rating equal to the max adapter rating + 3
    jolt_ratings = [0] + sorted(data) + [max(data)+3]

    return count_possible_combinations(jolt_ratings)

def main():
    data = [int(x) for x in load_input(__file__, 'input.txt')]

    assert(len(data) == len(set(data)))
    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()