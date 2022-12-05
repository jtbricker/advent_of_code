from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return data

def item_to_priority(item_char):
    if item_char.lower() == item_char:
        return ord(item_char) - 96
    return ord(item_char) - 38

def find_duplicated_item(comp_1, comp_2):
    comp_1 = set(comp_1)
    comp_2 = set(comp_2)

    dupes = comp_1.intersection(comp_2)
    assert len(dupes) == 1
    return list(dupes)[0]

def find_common_item(bp1, bp2, bp3):
    bp1 = set(bp1)
    bp2 = set(bp2)
    bp3 = set(bp3)

    dupes = bp1.intersection(bp2).intersection(bp3)
    assert len(dupes) == 1
    return list(dupes)[0]


def part_1(data):
    """Given a list of strings which represents items held in backpacks,
    determine the sum of priority values for items that appear in both compartments
    of the backpack.

    1) Each string in the input represents a backpack
    2) Each case-sensitive character in the string represents an item in a compartment of that backpack
    3) The first X/2 characters (where X is the length of the string) represent items in the first compartment of the backpack
        and the second X/2 characters represent items in the second compartment of the backpack
    4) Items a-z have priorities 1-26 and items A-Z have priorities 27-52
    5) Only a single duplicated item appears in each backpack

    Args:
        data (List[str]): List of backback strings

    Returns:
        [int]: Total priority sum of items found in both compartments of each backpack
    """
    data = parse_data(data)

    sum = 0
    for backpack in data:
        # print("Backpack length", len(backpack), backpack)
        compartment_1 = backpack[:len(backpack)//2]
        compartment_2 = backpack[len(backpack)//2:]
        dupe = find_duplicated_item(compartment_1, compartment_2)

        sum += item_to_priority(dupe)

    return sum

def part_2(data):
    """Given a list of strings which represents items held in backpacks,
    determine the sum of priority values of the item that exists in all backpacks
    within each set of 3 backpacks

    1) Each string in the input represents a backpack
    2) Each successive set of 3 backpacks represent a group of backpacks and in each group of backpack
        there is a single common item
    3) Each case-sensitive character in the string represents an item in that backpack
    4) Items a-z have priorities 1-26 and items A-Z have priorities 27-52
    5) Only a single duplicated item appears in each backpack

    Args:
        data (List[str]): List of backback strings

    Returns:
        [int]: Total priority sum of common item in each set of 3 backpacks
    """
    backpacks = parse_data(data)

    sum = 0
    for i in range(0, len(backpacks), 3):
        backpack1, backpack2, backpack3 = backpacks[i:i+3]
        dupe = find_common_item(backpack1, backpack2, backpack3)

        sum += item_to_priority(dupe)

    return sum

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()