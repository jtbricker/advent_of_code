from unittest import signals
from lib.helpers import load_input

def parse_data(data):
    # Override if you need to parse the data in
    # a particular way before doing work
    return [[y.split()  for y in x.split(' | ')] for x in data] 

def flatten(t):
    return [item for sublist in t for item in sublist]

def part_1(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = parse_data(data)

    four_digit_codes = flatten([x[1] for x in data])

    return len([x for x in four_digit_codes if len(x) in (2, 3, 4, 7)])

class SignalsCode:
    def __init__(self, data):
        self.signals = Signals(data[0])
        self.code = Code(data[1])

    def decode_code(self):
        mapping = self.signals.deduce()
        return self.code.decode(mapping)


class Signals:
    def __init__(self, signals):
        self.signals = ["".join(sorted(x)) for x in signals]
    
    def deduce(self):
        char_count = {}
        for sig in self.signals:
            for c in sig:
                count = char_count.get(c, 0)
                char_count[c] = count + 1

        bottom_left = [c for c,count in char_count.items() if count==4][0]

        sig_to_num_mapping = {}
        one_signals = None
        for s in self.signals:
            if len(s) == 2:
                sig_to_num_mapping[s]=1
                one_signals=s
            elif len(s) == 7:
                sig_to_num_mapping[s]=8
            elif len(s) == 3:
                sig_to_num_mapping[s]=7
            elif len(s) == 4:
                sig_to_num_mapping[s]=4

        for s in self.signals:
            if s in sig_to_num_mapping:
                pass
            if len(s) == 6:
                if one_signals[0] not in s or one_signals[1] not in s:
                    sig_to_num_mapping[s]=6
                else:
                    if bottom_left in s:
                        sig_to_num_mapping[s]=0
                    else:
                        sig_to_num_mapping[s]=9

            if len(s) == 5:
                if one_signals[0] in s and one_signals[1] in s:
                    sig_to_num_mapping[s]=3
                else:
                    if bottom_left in s:
                        sig_to_num_mapping[s]=2
                    else:
                        sig_to_num_mapping[s]=5
        return sig_to_num_mapping

class Code:
    def __init__(self, code):
        self.code = ["".join(sorted(x)) for x in code]

    def decode(self, mapping):
        return int("".join([str(mapping.get(c, c)) for c in self.code]))

def part_2(data):
    """[summary]

    Args:
        data ([type]): [description]

    Returns:
        [type]: [description]
    """
    data = [SignalsCode(x) for x in parse_data(data)]
    
    sum = 0
    for s in data:
        d = s.decode_code()
        print(d)
        sum += d
    return sum

def main():
    data = load_input(__file__)

    print(part_1(data))
    print(part_2(data))

if __name__ == "__main__":
    main()