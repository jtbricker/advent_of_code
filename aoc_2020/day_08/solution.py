from lib.helpers import load_input

def will_infinitely_loop(commands):
    accumulator = 0
    i = 0
    visited = []
    while True and i<len(commands):
        if i in visited:
            return True

        visited.append(i)

        command, val = commands[i].split()
        if command == 'acc':
            accumulator += int(val)
            i += 1
        elif command == 'jmp':
            i += int(val)
        else:
            i += 1

    return False

def get_program_result(commands):
    accumulator = 0
    i = 0
    visited = []
    while True and i<len(commands):
        if i in visited:
            print("Infinite Loop Detected. Returning acc value before command runs for 2nd time:")
            break

        visited.append(i)

        command, val = commands[i].split()
        if command == 'acc':
            accumulator += int(val)
            i += 1
        elif command == 'jmp':
            i += int(val)
        else:
            i += 1

    return accumulator

def part_1(data):
    """Print the value of the accumulator right before the command
    list input attempts to execute a command a second time
    (therefore starting an infinite loop)

    Args:
        data (list[str]): List of commands:
            acc [+- val]: increments the accumulator by the given value, go to next command
            jmp [+- val]: go to the command that is `val` ahead or behind
            nop [+- val]: do nothing, ignore val, go to next command

    """
    return get_program_result(data)
    

def part_2(data):
    """ Fix the commands so that it does not infinitely loop by swapping
    a jmp/nop for a nop/jmp and return the accumulator value of the fixed 
    set of commands

    Args:
        data (list[str]): List of commands:
            acc [+- val]: increments the accumulator by the given value, go to next command
            jmp [+- val]: go to the command that is `val` ahead or behind
            nop [+- val]: do nothing, ignore val, go to next command
    """
    for i in range(len(data)):
        if "nop" in data[i]:
            data[i] = data[i].replace("nop", "jmp")
            if not will_infinitely_loop(data):
                return get_program_result(data)
            else:
                data[i] = data[i].replace("jmp", "nop")
        
        if "jmp" in data[i]:
            data[i] = data[i].replace("jmp", "nop")
            if not will_infinitely_loop(data):
                return get_program_result(data)
            else:
                data[i] = data[i].replace("nop", "jmp")


def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()