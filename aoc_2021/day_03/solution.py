from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return data

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    num_bits = len(data[0])
    num_rows = len(data)
    print("Number of bits:", num_bits, "\tNumber of rows:", num_rows)
    most_common_bits = ""
    for i in range(num_bits):
        sum = 0
        for d in data:
            sum += int(d[i])
        if sum > (num_rows / 2):
            most_common_bits += '1'
        else:
            most_common_bits += '0'
    gamma_rate = int(most_common_bits, 2)
    epsilon_rate = int("0b"+"1"*num_bits, 2) - gamma_rate
    return gamma_rate * epsilon_rate


    

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    
    num_bits = len(data[0])

    rows = data.copy()
    for i in range(num_bits):
        print("Number of rows: ", len(rows))
        print(rows)
        if len(rows) == 1:
            break
        num_rows = len(rows)
        sum = 0
        for d in rows:
            sum += int(d[i])

        if sum >= (num_rows / 2):
            rows = [row for row in rows if row[i] == '1']
        else:
            rows = [row for row in rows if row[i] == '0']
    assert(len(rows) == 1)
    oxygen_generator_rating = int(rows[0], 2)

    rows = data.copy()
    for i in range(num_bits):
        if len(rows) == 1:
            break
        num_rows = len(rows)
        sum = 0
        for d in rows:
            sum += int(d[i])

        if sum >= (num_rows / 2):
            rows = [row for row in rows if row[i] == '0']
        else:
            rows = [row for row in rows if row[i] == '1']
    assert(len(rows) == 1)
    co2_scrubber_rating = int(rows[0], 2)
    
    return oxygen_generator_rating*co2_scrubber_rating

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()