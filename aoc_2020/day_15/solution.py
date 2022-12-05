from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return [int(x) for x in data[0].split(',')]

class MemoryGame:
    def __init__(self, seed_list, num_turns):
        self.seed_list_length = len(seed_list)
        self.list = [x for x in seed_list]
        self.num_turns = num_turns

    def run(self):
        for pos in range(self.seed_list_length, self.num_turns):
            self.add_next_num(pos)

        print(self.list)
        return self.list[-1]

    def add_next_num(self, pos):
        last_turn_number = len(self.list)
        last_num = self.list[-1]
        if last_num in self.list[:-1]:
            # The number has appeared in the list before
            most_recent_turn = len(self.list) - self.list[::-1].index(last_num, 1) 
            distance = last_turn_number - most_recent_turn
            self.list.append(distance)
        else:
            # This is the first time the number appears in the list
            self.list.append(0)


class MemoryGameV2:
    def __init__(self, seed_list, num_turns):
        self.most_recent_positions = {}
        self.seed_list_length = len(seed_list)
        self.list = [x for x in seed_list]
        self.num_turns = num_turns

        for i in range(len(seed_list)):
            self.most_recent_positions[i] = seed_list[i]
            print(seed_list[i])

        self.was_number_seen_before = False
        self.last_seen_before_distance = None
        self.most_recent_number = seed_list[-1]

    def run(self):
        for pos in range(self.seed_list_length, self.num_turns):
            self.add_next_num(pos)

        print(self.list)
        return self.most_recent_number

    def add_next_num(self, pos):
        if self.was_number_seen_before:
            # The number has appeared in the list before
            new_number = self.last_seen_before_distance

        else:
            # This is the first time the number appears in the list
            new_number = 0

        self.check_seen(new_number, pos)
        self.most_recent_number = new_number
        # print(self.most_recent_number)
        self.most_recent_positions[new_number] = pos
        self.list.append(self.most_recent_number)

    def check_seen(self, number, pos):
        if old_pos:=self.most_recent_positions.get(number):
            self.was_number_seen_before = True
            self.last_seen_before_distance = pos - old_pos
        else:
            self.was_number_seen_before = False
            self.last_seen_before_distance = None

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    result = MemoryGame(data, 20).run()
    result = MemoryGameV2(data, 20).run()
        
    return result

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    
    result = MemoryGameV2(data, 30000000).run()
        
    return result

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()