from lib.helpers import load_input

bump_neighbor_queue = []
flash_count = 0
DEBUG = False

class Octopus:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy
        self.has_flashed_this_round = False

    def bump(self):
        if not self.has_flashed_this_round:
            self.energy += 1

            if self.energy == 10:
                self.flash()

    def flash(self):
        global flash_count
        flash_count += 1
        self.has_flashed_this_round = True
        self.energy = 0
        self.queue_bump_neighbors()

    def queue_bump_neighbors(self):
        global bump_neighbor_queue
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if not(i == 0 and j==0):
                    bump_neighbor_queue.append((self.x+i, self.y+j))

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return [[int(x) for x in d] for d in data]

def step(octs):
    for oct in octs.values():
        oct.has_flashed_this_round = False

    for oct in octs.values():
        oct.bump()

    while len(bump_neighbor_queue) > 0:
        coord = bump_neighbor_queue.pop()
        try:
            oct = octs[coord]
            oct.bump()
        except KeyError:
            pass
    if DEBUG: print(bump_neighbor_queue) 

def print_octs(octs):
    y_str = ''
    for i in range(10):
        x_str = ''
        for j in range(10):
            oct = octs[(i,j)]
            x_str += str(oct.energy)
        y_str += x_str + "\n"
    print(y_str)

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    octs = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            octs[(i,j)] = Octopus(i,j,data[i][j])

    if DEBUG:
        print("Before any steps:")
        print_octs(octs)

    for i in range(100):
        step(octs)
        if DEBUG:
            print(f"After step {i+1}:")
            print_octs(octs)
    return flash_count

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    octs = {}
    for i in range(len(data)):
        for j in range(len(data[0])):
            octs[(i,j)] = Octopus(i,j,data[i][j])
    
    step_num = 0
    while not check_all_flashed(octs):
        step(octs)
        step_num += 1
        
    return step_num

def check_all_flashed(octs):
    for i in range(10):
        for j in range(10):
            if octs[(i,j)].energy != 0:
                return False

    return True

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()