from lib.helpers import load_input

def part_1(data):
    """ Find the first number that does not respect the property
    that all numbers after the first 25 must be the sum of two of 
    the numbers from the previous 25 numbers.

    Args:
        data (list[int]): List of numbers
    """

    sums = []
    for i in range(25):
        for j in range(i, 25):
            sums.append(data[i]+data[j])
    
    for i in range(25, len(data)):
        if data[i] not in sums:
            return data[i]
        else:
            sums = [data[x] + data[y] for x in range(i+1-25, i+1) for y in range(i+1-25+1, i+1)]

def part_2(data, invalid_number):
    """Find the sum of the smallest and largest numbers in a contiguous set of numbers
    from the data set that add to the provided number

    Args:
        data (list[int]): List of numbers
        invalid_number (int): number to target

    Returns:
        int: Sum of the smallest and largest numbers that add to the invalid_number
    """
    
    for i in range(len(data)):
        cont_nums = [data[i]]
        j = i+1
        while sum(cont_nums) < invalid_number:
            cont_nums.append(data[j])
            j += 1

        if sum(cont_nums) == invalid_number:
            return min(cont_nums) + max(cont_nums)


def main():
    data = [int(x) for x in load_input(__file__)]

    invalid_number = part_1(data)
    print(invalid_number)
    print(part_2(data, invalid_number))

if __name__ == "__main__":
    main()