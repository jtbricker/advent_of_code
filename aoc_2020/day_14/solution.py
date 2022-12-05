from typing import Dict, List
from lib.helpers import load_input


def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return data

class Command:
    def __init__(self):
        self.memory_bank = {}

    def set_mask(self, raw_command):
        mask: str = raw_command.split('=')[1].strip()
        self.on_mask_num: int = int(''.join(['1' if i=='1' else '0' for i in mask]), 2)
        self.off_mask_num: int = int(''.join(['0' if i=='0' else '1' for i in mask]), 2)

    def set_memory(self, raw_command):
        mem_loc = int(raw_command.strip().split(']')[0][4:])
        value = int(raw_command.split('=')[1].strip())

        self.memory_bank[mem_loc] = (value & self.off_mask_num) | self.on_mask_num

class Command2:
    def __init__(self):
        self.memory_bank = {}

    def set_mask(self, raw_command):
        self.mask: str = raw_command.split('=')[1].strip()

    def set_memory(self, raw_command):
        mem_loc = int(raw_command.strip().split(']')[0][4:])
        value = int(raw_command.split('=')[1].strip())

        decoded_mem_locs = self.decode_memory(mem_loc)
        for d in decoded_mem_locs:
            self.memory_bank[d] = value

    def decode_memory(self, mem_loc):
        masked_mem_loc = ''
        binary_mem_loc = bin(mem_loc)[2:].zfill(36)
        for i in range(36):
            if self.mask[i].upper() == 'X':
                masked_mem_loc += 'X'
            elif self.mask[i] == '0':
                masked_mem_loc += binary_mem_loc[i]
            elif self.mask[i] == '1':
                masked_mem_loc += '1'
            else:
                raise Exception("Something wierd happened")

        mem_locs = ['']
        for x in masked_mem_loc:
            new_mem_locs = []
            if x.upper() == 'X':
                for y in mem_locs:
                    new_mem_locs.append(y+'0')
                    new_mem_locs.append(y+'1')
                mem_locs = new_mem_locs.copy()
            else:
                for y in mem_locs:
                    new_mem_locs.append(y+x)
                mem_locs = new_mem_locs.copy()

        return [int(x, 2) for x in mem_locs]


def part_1(data: List[str]) -> int:
    """Determine the sum of non-zero memory values after memory operations 
    using masks

    Args:
        data (List[str]): List of commands where command is either:
            - A memory assignment of form: "mem[X]=Y, where X is memory location and Y is mask adjusted int
            - A new mask to apply in memory assignment operations

    Returns:
        [int]: Sum of non-zero memory values after all operations
    """
    data = parse_data(data)
    process = Command()
    for command in data:
        if 'mask' in command:
            process.set_mask(command)
        else:
            process.set_memory(command)

    return sum(process.memory_bank.values())


def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)
    process = Command2()
    for command in data:
        if 'mask' in command:
            process.set_mask(command)
        else:
            process.set_memory(command)

    return sum(process.memory_bank.values())

def main():
    data = load_input(__file__)
    
    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()
