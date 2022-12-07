from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return data

def find_first_non_repeating_window_position(str, window_size):
    window = str[:window_size]
    # print("str",str)
    i = window_size
    while i < len(str) - 1:
        # print("i",i,"window",window)
        if len(window) == len(set(window)):
            return i
        window = window[1:] + str[i]
        i +=1
        
    raise Exception(f"No non-repeating window of size {window_size} was found.")


def part_1(data):
    """ Given a string find the position of the first character
        in which the rolling window of 4 characters does not repeat

    Args:
        data (str): String of characters

    Returns:
        int: first position in which the rolling window of 4 characters does not repeat
    """
    data = parse_data(data)
    if isinstance(data, list):
        data = data[0]

    return find_first_non_repeating_window_position(data, window_size=4)

def part_2(data):
    """ Given a string find the position of the first character
        in which the rolling window of 14 characters does not repeat

    Args:
        data (str): String of characters

    Returns:
        int: first position in which the rolling window of 4 characters does not repeat
    """
    data = parse_data(data)
    if isinstance(data, list):
        data = data[0]

    return find_first_non_repeating_window_position(data, window_size=14)

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()