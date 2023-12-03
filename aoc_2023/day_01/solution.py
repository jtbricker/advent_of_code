from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return data

def part_1(data):
    """ Given a list of string that contain numbers,
    return the sum of the first and last number in each string

    Args:
        data (list(str)): List of strings that contain numbers

    Returns:
        int: Sum of the first and last number in each string
    """
    data = parse_data(data)

    total = 0
    for d in data:
        nums = "".join([x for x in d if x.isdigit()])
        total += int(nums[0] + nums[-1])
    return total

number_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven":7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

def part_2(data):
    """ Given a list of strings that contain numbers (some spelled out),
    return the sum of the first and last number in each string

    Args:
        data (list(str)): List of strings that contain numbers (some spelled out)

    Returns:
        int: Sum of the first and last number in each string
    """
    data = parse_data(data)

    for key, value in number_map.items():
        data = [d.replace(key, key+str(value)+key) for d in data]

    total = 0
    for d in data:
        nums = "".join([x for x in d if x.isdigit()])
        total += int(nums[0] + nums[-1])
    return total

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()