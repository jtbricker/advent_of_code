from datetime import time
import math

from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    timestamp = int(data[0])
    buses = data[1].split(',')
    return timestamp, buses

def part_1(data):
    """What is the ID of the earliest bus you can take to the airport 
    multiplied by the number of minutes you'll need to wait for that bus?

    Args:
        data (list(str)): List of 2 strings

        First String: Timestamp (integer) from a fixed point in time when I arrive at bus station
        Second String: Comma seperated list of bus ids (X), which run every X minutes from 
                        the same fixed point in time

    Returns:
        int: The number of minutes waited for the earliest bus multiplied by the bus id
    """
    timestamp, buses = parse_data(data)

    min_wait = None
    earliest_bus = None
    for bus in buses:
        if bus == 'x':
            pass
        else:
            bus = int(bus)
            wait = bus - (timestamp % bus)
            if min_wait is None or min_wait > wait:
                min_wait = wait
                earliest_bus = bus
    return min_wait*earliest_bus

def are_buses_sequential(buses, timestamp):
    for i in range(1, len(buses)):
        if buses[i] != 'x' and (timestamp+i)%int(buses[i]) != 0:
            return False
    return True

def part_2(data):
    """What is the earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list?

    Args:
        data (list(str)): List of 2 strings

        First String: Timestamp (integer) from a fixed point in time when I arrive at bus station
        Second String: Comma seperated list of bus ids (X), which run every X minutes from 
                        the same fixed point in time

    Returns:
        int: "The time where all the buses arrive at the right offsets."
    """
    _, buses = parse_data(data)
    
    time = int(buses[0])
    step = 1
    schedule = {t: int(id) for t, id in enumerate(buses) if id != 'x'}
    for t in schedule:
        while (time +t) % schedule[t] != 0:
            time += step
        step *= schedule[t]
    return time
            
    



def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()