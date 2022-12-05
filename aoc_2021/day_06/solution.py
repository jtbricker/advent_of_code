from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    data = [int(x) for x in data[0].split(',')]
    fishes = {}
    for d in data:
        count = fishes.get(d,0)
        fishes[d] = count + 1
    return fishes

def next_day(fishes):
    new_fishes = {}
    for day in fishes.keys():
        if day == 0:
            # These fish have each produced a new fish and reset their timer
            new_fishes[6] = new_fishes.get(6, 0) + fishes[day]
            new_fishes[8] = fishes[day]
        else:
            new_fishes[day-1] = new_fishes.get(day-1, 0) + fishes[day]
    return new_fishes

def part_1(data):
    """Given a list of fish reproduction timers, simulate them number of fish
    present after 80 days given the following rules:

    * Fish reproduce every 7 days, producing a fish with a timer of 9 days (two day 
        buffer before starting to reproduce)
    * Every "day", a fish's reproductive timer decreases by 1
    * If a fish's timer is at 0 before the update, it resets to 6 and produces a new fish 
        (with timer 8)

    Args:
        data (List[ints]): List of initial fish timers

    Returns:
        int: Number of fish present in the system after 80 days
    """
    NUM_DAYS = 80

    fishes = parse_data(data)    
    
    for _ in range(NUM_DAYS):
        fishes = next_day(fishes)

    return sum(fishes.values())

def part_2(data):
    """Given a list of fish reproduction timers, simulate them number of fish
    present after 256 days given the following rules:

    * Fish reproduce every 7 days, producing a fish with a timer of 9 days (two day 
        buffer before starting to reproduce)
    * Every "day", a fish's reproductive timer decreases by 1
    * If a fish's timer is at 0 before the update, it resets to 6 and produces a new fish 
        (with timer 8)

    Args:
        data (List[ints]): List of initial fish timers

    Returns:
        int: Number of fish present in the system after 256 days
    """
    NUM_DAYS = 256
    fishes = parse_data(data)
    
    for _ in range(NUM_DAYS):
        fishes = next_day(fishes)

    return sum(fishes.values())

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()