from lib.helpers import (
    load_input_chunked
)

def part_1(data):
    """ For each group, get count of distinct elements in union of all characters in all group members strings.
    Return the total count for all groups.

    Args:
        data (list(list(str))): Groups of questionaire answers, where group members answers are elements of the inner list
        and represented by the question letters to which they answered 'yes'
    """
    count = 0
    for group in data:
        count += len(set.union(*[set(answers) for answers in group]))
    return count

def part_2(data):
    """ For each group, get count of distinct elements in intersection of all characters in all group members strings.
    Return the total count for all groups.

    Args:
        data (list(list(str))): Groups of questionaire answers, where group members answers are elements of the inner list
        and represented by the question letters to which they answered 'yes'
    """
    count = 0
    for group in data:
        count += len(set.intersection(*[set(answers) for answers in group]))
    return count

def main():
    data = load_input_chunked(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()