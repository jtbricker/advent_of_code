from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    data = data[0].split(': ')[1].split(', ')
    x_data = [int(x) for x in data[0][2:].split('..')]
    y_data = [int(x) for x in data[1][2:].split('..')]

    x_min, x_max = x_data
    y_min, y_max = y_data
    return (x_min, x_max, y_min, y_max)

class Physics:
    def __init__(self, vx, vy, min_x, max_x, min_y, max_y):
        self.vx = vx
        self.vy = vy
        self.pos_x = 0
        self.pos_y = 0
        self.min_x, self.max_x, self.min_y, self.max_y = min_x, max_x, min_y, max_y

    def step(self):
        self.pos_x += self.vx
        self.pos_y += self.vy

        if self.vx < 0:
            self.vx += 1
        elif self.vx > 0:
            self.vx -= 1

        self.vy -= 1

    def in_target(self):
        if self.min_x <= self.pos_x <= self.max_x and self.min_y <= self.pos_y <= self.max_y:
            return True
        return False

    def run(self):
        max_y = 0
        while self.pos_y >= self.min_y and not self.in_target():
            self.step()
            if self.pos_y > max_y:
                max_y = self.pos_y
        
        if self.in_target():
            return max_y
        return -1

    def run2(self):
        while self.pos_y >= self.min_y and not self.in_target():
            self.step()
        
        if self.in_target():
            return True
        return False


def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    max_y = 0
    for vx in range(1,data[1]+1):
        for vy in range(data[2], -data[2]+1):
            p = Physics(vx,vy, data[0], data[1], data[2], data[3])
            run_max_y = p.run()
            if run_max_y > max_y:
                max_y = run_max_y
    return max_y

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    count = 0
    min_vx = 1
    max_vx = data[1]+1
    min_vy = data[2]
    max_vy = -data[2]+1
    print("min_vx", min_vx, "max_vx", max_vx, "min_vy", min_vy, "max_vy", max_vy)
    for vx in range(min_vx, max_vx):
        for vy in range(min_vy, max_vy):
            p = Physics(vx,vy, data[0], data[1], data[2], data[3])
            if p.run2():
                print(vx, vy)
                count += 1
    return count

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()