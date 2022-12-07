from lib.helpers import load_input_raw

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    num_columns = len(data[0])//4
    columns = { x: [] for x in range(1, num_columns+1)}
    
    x = 0
    while data[x].strip()[0] != '1':
        for i in range(num_columns):
            col = i+1
            entry = data[x][4*i+1].strip()
            if entry:
                columns[col].insert(0,entry)
        x += 1
    
    instructions = []
    for d in data[x+2:]:
        parts = d.split(' ')
        instructions.append({
            'count': int(parts[1]),
            'from': int(parts[3]),
            'to': int(parts[5]),
        })
    
    return columns, instructions

def make_move(columns, instruction):
    to = instruction['to']
    from_ = instruction['from']
    count = instruction['count']

    for i in range(count):
        item = columns[from_].pop()
        columns[to].append(item)
    return columns

def make_move_2(columns, instruction):
    to = instruction['to']
    from_ = instruction['from']
    count = instruction['count']

    items_to_move = columns[from_][-1*count:]
    columns[from_] = columns[from_][:-1*count]
    columns[to] += items_to_move
    return columns

def part_1(data):
    """ Given a set of items stacked in columns and a set of instructiions for
    moving a certain number of items (represented by a single character) from the
     top of one stack to the top of another stack, determine the top items in each stack

    Args:
        data (List[str]): An ascii image representing the initial state of the columns of items,
            followed by a blank line, followed by a series of instructions (one on each line)

            Instructions include `from` and `to` (representing where items are moving) and
                count (representing the number of items to move, one at a time)

    Returns:
        str: A string representing the top items from each column (in order) with no spaces
    """
    columns, instructions = parse_data(data)

    for inst in instructions:
        columns = make_move(columns, inst)
    
    top_items = ""
    for i in range(1, len(columns)+1):
        top_items += columns[i][-1]
    return top_items

def part_2(data):
    """ Given a set of items stacked in columns and a set of instructiions for
    moving a certain number of items (represented by a single character) from the
     top of one stack to the top of another stack, determine the top items in each stack

    Args:
        data (List[str]): An ascii image representing the initial state of the columns of items,
            followed by a blank line, followed by a series of instructions (one on each line)

            Instructions include `from` and `to` (representing where items are moving) and
                count (representing the number of items to move, ***** ALL AT ONCE ****)

    Returns:
        str: A string representing the top items from each column (in order) with no spaces
    """
    columns, instructions = parse_data(data)

    for inst in instructions:
        columns = make_move_2(columns, inst)
    
    top_items = ""
    for i in range(1, len(columns)+1):
        top_items += columns[i][-1]
    return top_items

def main():
    data = load_input_raw(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()